from django.db.models import Q
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
)
from blog.paginations import PostLimitOffsetPagination, PostPageNumberPagination
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    AllowAny, IsAuthenticated,
)

from .models import Comment
from .serializers import (
    CommentListSerializer, CommentDetailSerializer, create_comment_serializer
)


class CommentListAPIView(ListAPIView):
    '''
    API endpoint that allows ALL users view all the posts
    '''
    serializer_class = CommentListSerializer
    permission_classes = (AllowAny, )
    lookup_field = 'id'
    '''
    sorted queryset with search fields (?search='')
    ordered queryset with search fields (?order='')
    '''
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['content', 'publish']
    '''
    PagePagination -> ?page=2
    '''
    pagination_class = PostPageNumberPagination

    def get_queryset(self, *args, **kwargs):
        queryset_list = Comment.objects.all()
        '''
        sorted queryset with query params (?query="")
        '''
        query = self.request.GET.get('query')
        if query:
            queryset_list = queryset_list.filter(
                Q(content__icontains=query) |
                Q(user__first_name__icontains=query) |
                Q(user__last_name__icontains=query)
            ).distinct()

        return queryset_list


class CommentCreateAPIView(CreateAPIView):
    '''
    API endpoint that allows ADMIN users create posts
    '''
    queryset = Comment.objects.all()
    permission_classes = (IsAuthenticated, )

    def get_serializer_class(self):
        model_type = self.request.query_params.get('type', 'post')
        slug = self.request.query_params.get('slug')
        parent_id = self.request.query_params.get('parent_id')

        return create_comment_serializer(
            model_type=model_type,
            slug=slug,
            parent_id=parent_id,
        )
    
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class CommentDetailAPIView(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    '''
    API endpoint that allows All users view the define post
    '''
    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)




