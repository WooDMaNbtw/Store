from django.db.models import Q
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView, RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import (
    AllowAny, IsAdminUser,
)
from django.contrib.auth.models import User
from .models import Experience, Information
from .serializers import (
    BiographyListSerializer,
    BiographyDetailSerializer,
    BiographyCreateSerializer,
    BiographyInfoSerializer,
    BiographyInfoCreateSerializer
)


class BiographyListAPIView(ListAPIView):
    serializer_class = BiographyListSerializer
    permission_classes = (AllowAny,)

    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('title', 'position')

    def get_queryset(self):
        queryset_list = Experience.objects.all()

        query = self.request.GET.get('query')
        if query:
            queryset_list = queryset_list.filter(
                Q(title__icontains=query) |
                Q(position__icontains=query)
            ).distinct()

        return queryset_list


class BiographyCreateAPIView(CreateAPIView):

    queryset = Experience.objects.all()
    serializer_class = BiographyCreateSerializer
    permission_classes = (IsAdminUser, )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BiographyDetailAPIView(RetrieveAPIView):
    queryset = Experience.objects.all()
    serializer_class = BiographyDetailSerializer
    permission_classes = (AllowAny, )
    lookup_field = 'slug'


class BiographyUpdateAPIView(RetrieveAPIView, UpdateAPIView, DestroyAPIView):

    queryset = Experience.objects.all()
    serializer_class = BiographyDetailSerializer
    permission_classes = (IsAdminUser, )
    lookup_field = 'slug'


class BiographyInfoAPIView(ListAPIView):

    queryset = Information.objects.all()
    serializer_class = BiographyInfoSerializer
    permission_classes = (AllowAny, )


class BiographyInfoCreateAPIView(CreateAPIView):

    queryset = Information.objects.all()
    serializer_class = BiographyInfoCreateSerializer
    permission_classes = (IsAdminUser, )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BiographyInfoDetailAPIView(RetrieveUpdateDestroyAPIView):

    queryset = Information.objects.all()
    serializer_class = BiographyInfoSerializer
    permission_classes = (IsAdminUser, )
    lookup_field = "id"






