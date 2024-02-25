from django.urls import path

from .views import (
    PostListAPIView,
    PostCreateAPIView,
    PostDetailAPIView,
    PostUpdateAPIView,
    PostDeleteAPIView
)

urlpatterns = [
    path("", PostListAPIView.as_view(), name='list'),
    path("create/", PostCreateAPIView.as_view(), name='create'),
    path("<slug:slug>", PostDetailAPIView.as_view(), name='detail'),
    path("<slug:slug>/update", PostUpdateAPIView.as_view(), name='update'),
    path("<slug:slug>/delete", PostDeleteAPIView.as_view(), name='delete')
]
