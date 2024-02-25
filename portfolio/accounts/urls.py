from django.urls import path

from .views import (
    UserCreateAPIView,
    UserLoginAPIView
)

urlpatterns = [
    path('create/', UserCreateAPIView.as_view(), name='create'),
    path('login/', UserLoginAPIView.as_view(), name='login'),
    path('logout/', UserLoginAPIView.as_view(), name='login'),
]