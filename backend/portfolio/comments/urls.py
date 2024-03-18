from django.urls import path
from .views import (
    CommentListAPIView,
    CommentCreateAPIView,
    CommentDetailAPIView,
)

urlpatterns = [
    path('', CommentListAPIView.as_view(), name='list'),
    path('create/', CommentCreateAPIView.as_view(), name='create'),
    path('<int:pk>/', CommentDetailAPIView.as_view(), name='detail'),
]
