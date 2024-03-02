from django.urls import path
from .views import (
    ProjectListAPIView,
    ProjectDetailAPIView,
    ProjectCreateAPIView,
    ProjectUpdateAPIView
)

urlpatterns = [
    path('', ProjectListAPIView.as_view(), name='project-list'),
    path('create/', ProjectCreateAPIView.as_view(), name='project-create'),
    path('<int:id>/', ProjectDetailAPIView.as_view(), name='project-detail'),
    path('<int:id>/update', ProjectUpdateAPIView.as_view(), name='project-update'),
]
