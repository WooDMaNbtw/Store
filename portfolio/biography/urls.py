from django.urls import path
from .views import (
    BiographyListAPIView,
    BiographyCreateAPIView,
    BiographyDetailAPIView,
    BiographyUpdateAPIView
)

urlpatterns = [
    path('', BiographyListAPIView.as_view(), name='bio-list'),
    path('create/', BiographyCreateAPIView.as_view(), name='bio-create'),
    path('<slug:slug>/', BiographyDetailAPIView.as_view(), name='bio-detail'),
    path('<slug:slug>/update', BiographyUpdateAPIView.as_view(), name='bio-update')
]
