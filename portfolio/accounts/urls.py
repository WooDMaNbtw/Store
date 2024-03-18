from django.urls import path, include
from .views import CustomTokenObtainPairView

urlpatterns = [
    path("auth/jwt/create/", CustomTokenObtainPairView.as_view(), name="custom-jwt-create"),
    path("auth/", include('djoser.urls')),
    path("auth/", include('djoser.urls.jwt'))
]
