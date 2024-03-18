from rest_framework import serializers
from .models import Experience, Information
from accounts.serializers import UserSerializer
from projects.models import Project
from projects.serializers import ProjectDetailSerializer


class BiographyListSerializer(serializers.ModelSerializer):
    # projects_count = serializers.SerializerMethodField()
    url = serializers.HyperlinkedIdentityField(
        view_name='bio-detail',
        lookup_field='slug',
    )

    class Meta:
        model = Experience
        fields = ('url', 'slug', 'title', 'company', 'position', 'description')

    @staticmethod
    def get_projects_count(obj):
        if obj is not None:
            project_obj = Project.objects.filter(experience=obj.id)
            return project_obj.count()
        return 0


class BiographyCreateSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True)
    position = serializers.CharField(required=True)
    begin_time = serializers.DateField(required=True)

    class Meta:
        model = Experience
        fields = ('user', 'title', 'company', 'position', 'description', 'begin_time', 'end_time')
        read_only_fields = ('user', )

    def validate(self, data):
        title = data.get('title')
        experience_queryset = Experience.objects.filter(title__iexact=title)
        if experience_queryset.exists():
            raise serializers.ValidationError("Experience with this title already exists")
        return data


class BiographyDetailSerializer(serializers.ModelSerializer):
    projects = serializers.SerializerMethodField()
    user = UserSerializer(read_only=True)

    class Meta:
        model = Experience
        fields = ('user', 'title', 'company',
                  'position', 'description', 'begin_time',
                  'end_time', 'projects')

    @staticmethod
    def get_projects(obj):
        if obj is not None:
            project_obj = Project.objects.filter(experience=obj.id)
            return ProjectDetailSerializer(project_obj, many=True).data
        return None


class BiographyInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Information
        fields = '__all__'


class BiographyInfoCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Information
        fields = '__all__'
        read_only_fields = ('user', )
