from django.db.models import Q
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
)
from rest_framework.permissions import (
    AllowAny, IsAdminUser,
)

from .models import Project
from .serializers import (
    ProjectListSerializer,
    ProjectDetailSerializer,
    ProjectCreateSerializer
)


class ProjectListAPIView(ListAPIView):

    serializer_class = ProjectListSerializer
    permission_classes = (AllowAny, )

    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('title', )

    def get_queryset(self):
        queryset = Project.objects.all()

        query = self.request.GET.get('query')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query)
            ).distinct()

        return queryset


class ProjectCreateAPIView(CreateAPIView):

    queryset = Project.objects.all()
    serializer_class = ProjectCreateSerializer
    permission_classes = (IsAdminUser, )


class ProjectDetailAPIView(RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerializer
    permission_classes = (AllowAny, )
    lookup_field = "id"


class ProjectUpdateAPIView(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerializer
    permission_classes = (IsAdminUser, )
    lookup_field = "id"
