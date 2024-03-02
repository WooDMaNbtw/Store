from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from .models import Comment
from accounts.serializers import UserDetailSerializer


def create_comment_serializer(model_type='post', slug=None, parent_id=None, user=None):

    class CommentCreateSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = (
                'id',
                'parent',
                'content',
                'timestamp',
            )

        def __init__(self, *args, **kwargs):
            self.model_type = model_type
            print(model_type)
            self.slug = slug
            self.user = user
            self.parent_obj = None
            if parent_id:
                parent_queryset = Comment.objects.filter(id=parent_id)
                if parent_queryset.exists() and parent_queryset.count() == 1:
                    self.parent_obj = parent_queryset.first()

            super(CommentCreateSerializer, self).__init__(*args, **kwargs)

        def validate(self, data):
            model_type = self.model_type
            model_queryset = ContentType.objects.filter(model=model_type)
            if not model_queryset.exists() or model_queryset.count() != 1:
                raise serializers.ValidationError("This is not valid content type!")
            SomeModel = model_queryset.first().model_class()
            obj_queryset = SomeModel.objects.filter(slug=self.slug)
            if not obj_queryset.exists() or obj_queryset.count() != 1:
                raise serializers.ValidationError("This is not valid slug for this content type!")
            return data

        def create(self, validated_data):
            content = validated_data.get("content")
            user = self.user if self.user else User.objects.all().first()
            model_type = self.model_type
            slug = self.slug
            parent_obj = self.parent_obj

            comment = Comment.objects.create_by_model_type(
                model_type=model_type,
                slug=slug,
                content=content,
                user=user,
                parent_obj=parent_obj
            )

            return comment

    return CommentCreateSerializer


class __BaseCommentSerializer(serializers.ModelSerializer):

    user = UserDetailSerializer()
    replies_count = None
    replies = None
    content_object_url = None
    meta_fields = None

    @staticmethod
    def get_replies(obj):
        if obj is not None and obj.is_parent:
            return CommentChildSerializer(obj.children(), many=True).data
        return None

    @staticmethod
    def get_replies_count(obj):
        if obj is not None and obj.is_parent:
            return obj.children().count()
        return 0

    @staticmethod
    def get_content_object_url(obj):
        if obj is not None:
            try:
                return obj.content_object.get_api_url()
            except AttributeError:
                return None
        return None


class CommentListSerializer(__BaseCommentSerializer):

    replies_count = SerializerMethodField()

    class Meta:
        model = Comment
        fields = (
            'id',
            'user',
            'content',
            'replies_count',
            'timestamp',
        )


class CommentDetailSerializer(__BaseCommentSerializer):

    content_object_url = SerializerMethodField()
    replies_count = SerializerMethodField()
    replies = SerializerMethodField()

    class Meta:
        model = Comment
        fields = (
            'id',
            'user',
            'content',
            'replies_count',
            'replies',
            'timestamp',
            'content_object_url',
        )
        read_only_fields = (
            'reply_count',
            'replies'
        )


class CommentChildSerializer(__BaseCommentSerializer):

    class Meta:
        model = Comment
        fields = (
            'id',
            'user',
            'content',
            'parent',
            'timestamp'
        )


