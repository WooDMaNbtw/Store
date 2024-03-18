from django.db.models import Q
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
)
from .paginations import PostPageNumberPagination
from rest_framework.permissions import (
    IsAdminUser,
    AllowAny, IsAuthenticated,
)

from .models import Post
from .serializers import (
    PostListSerializer,
    PostCreateSerializer,
    PostDetailSerializer
)


class PostListAPIView(ListAPIView):
    """
    API endpoint that allows ALL users view all the posts
    """
    serializer_class = PostListSerializer
    permission_classes = [AllowAny, ]
    '''
    sorted queryset with search fields (?search='')
    ordered queryset with search fields (?order='')
    '''
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'content', 'publish']
    '''
    PagePagination -> ?page=2
    '''
    pagination_class = PostPageNumberPagination

    def get_queryset(self, *args, **kwargs):
        queryset_list = Post.objects.all()
        '''
        sorted queryset with query params (?query="")
        '''
        query = self.request.GET.get('query')
        if query:
            queryset_list = queryset_list.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(user__first_name__icontains=query) |
                Q(user__last_name__icontains=query)
            ).distinct()

        return queryset_list


class PostCreateAPIView(CreateAPIView):
    """
    API endpoint that allows ADMIN users create posts
    """
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostDetailAPIView(RetrieveAPIView):
    """
    API endpoint that allows All users view the define post
    """
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = (AllowAny, )
    lookup_field = 'slug'


class PostUpdateAPIView(UpdateAPIView):
    """
    API endpoint that allows ADMIN users update the define post
    """
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'
    permission_classes = (IsAdminUser, )

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class PostDeleteAPIView(DestroyAPIView):
    '''
    API endpoint that allows ADMIN users delete the define post
    '''
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = (IsAdminUser, )
    lookup_field = 'slug'
