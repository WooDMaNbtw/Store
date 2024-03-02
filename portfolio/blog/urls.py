from django.urls import path
from .views import (
    PostListAPIView,
    PostCreateAPIView,
    PostDetailAPIView,
    PostUpdateAPIView,
    PostDeleteAPIView
)

urlpatterns = [
    path("", PostListAPIView.as_view(), name='blog-list'),
    path("create/", PostCreateAPIView.as_view(), name='blog-create'),
    path("<slug:slug>", PostDetailAPIView.as_view(), name='blog-detail'),
    path("<slug:slug>/update", PostUpdateAPIView.as_view(), name='blog-update'),
    path("<slug:slug>/delete", PostDeleteAPIView.as_view(), name='blog-delete')
]
