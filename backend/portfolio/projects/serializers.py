from rest_framework import serializers
from .models import Project
from biography.models import Experience


class ShortExperienceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Experience
        fields = ('company', 'position', 'title')


class ProjectListSerializer(serializers.ModelSerializer):
    experience = ShortExperienceSerializer()
    url = serializers.HyperlinkedIdentityField(
        view_name='project-detail',
        lookup_field='id'
    )

    class Meta:
        model = Project
        fields = (
            'id',
            'url',
            'title',
            'link',
            'description',
            'experience',
        )


class ProjectCreateSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True)

    class Meta:
        model = Project
        fields = (
            'experience',
            'title',
            'link',
            'description',
        )


class ProjectDetailSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True)

    class Meta:
        model = Project
        fields = (
            'title',
            'link',
            'description',
        )

