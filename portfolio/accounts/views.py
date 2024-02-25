from django.contrib.auth.models import User
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
)
from blog.paginations import PostLimitOffsetPagination, PostPageNumberPagination
from rest_framework.permissions import (
    IsAdminUser,
    AllowAny,
    IsAuthenticatedOrReadOnly,
)

from .serializers import UserCreateSerializer, UserLoginSerializer


class UserCreateAPIView(CreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserLoginAPIView(APIView):

    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            response_data = serializer.data
            return Response(response_data, status=HTTP_200_OK)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


