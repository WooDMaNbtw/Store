from django.urls import path
from .views import (
    BiographyListAPIView,
    BiographyCreateAPIView,
    BiographyDetailAPIView,
    BiographyUpdateAPIView,
    BiographyInfoAPIView,
    BiographyInfoDetailAPIView,
    BiographyInfoCreateAPIView
)

urlpatterns = [
    path('', BiographyListAPIView.as_view(), name='bio-list'),
    path('create/', BiographyCreateAPIView.as_view(), name='bio-create'),
    path('<slug:slug>/', BiographyDetailAPIView.as_view(), name='bio-detail'),
    path('<slug:slug>/update', BiographyUpdateAPIView.as_view(), name='bio-update'),
    path('about/info/', BiographyInfoAPIView.as_view(), name='bio-info'),
    path('about/info/create/', BiographyInfoCreateAPIView.as_view(), name='bio-info-create'),
    path('about/info/<int:id>/', BiographyInfoDetailAPIView.as_view(), name='bio-info-edit'),
]
