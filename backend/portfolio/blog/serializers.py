from rest_framework import serializers
from .models import Post
from accounts.serializers import UserSerializer
from comments.serializers import CommentListSerializer


class PostListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='blog-detail',
        lookup_field='slug'
    )
    user = UserSerializer(read_only=True)
    image = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            'id',
            'url',
            'user',
            'slug',
            'title',
            'content',
            'publish',
            'comments',
            'image'
        )

    @staticmethod
    def get_image(obj):
        try:
            image = obj.image.url
        except Exception as ex:
            image = None

        return image

    @staticmethod
    def get_comments(obj):
        comments = obj.comment_set.all()
        return CommentListSerializer(comments, many=True).data


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'title',
            'content',
        )

    def validate(self, data):
        title = data.get('title')
        content = data.get('content')
        if not content or not title:
            raise serializers.ValidationError('You must provide a title and content')

        if len(title) > 50:
            raise serializers.ValidationError('Title is too long')

        return data


class PostDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            'id',
            'user',
            'title',
            'content',
            'publish',
            'comments'
        )

    @staticmethod
    def get_comments(obj):
        comments = obj.comment_set.all()
        return CommentListSerializer(comments, many=True).data

