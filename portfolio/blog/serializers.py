from rest_framework import serializers

from .models import Post
from accounts.serializers import UserDetailSerializer


class PostListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='detail',
        lookup_field='slug'
    )
    user = UserDetailSerializer(read_only=True)
    image = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            'id',
            'url',
            'user',
            'title',
            'content',
            'publish',
            'image'
        )

    @staticmethod
    def get_image(obj):
        try:
            image = obj.image.url
        except Exception as ex:
            image = None

        return image


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'title',
            'content',
        )


class PostDetailSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer(read_only=True)

    class Meta:
        model = Post
        fields = (
            'id',
            'user',
            'title',
            'content',
            'publish'
        )

