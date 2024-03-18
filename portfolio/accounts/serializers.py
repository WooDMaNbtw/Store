from accounts.models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model
from djoser.serializers import (
    UserSerializer as BaseUserSerializer,
    UserCreateSerializer as BaseUserCreateSerializer
)

user = get_user_model()


class UserCreateSerializer(BaseUserCreateSerializer):
    email = serializers.EmailField(required=True)

    class Meta(BaseUserSerializer.Meta):
        fields = (
            'email',
            'password'
        )
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': 'text'
                }
            }
        }

    def validate(self, attrs):
        # Validate uniqueness of email
        email = attrs.get('email')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('User with this email already exists.')
        return attrs


class UserSerializer(BaseUserSerializer):

    class Meta(BaseUserSerializer.Meta):
        fields = (
            'id',
            'username',
            'email',
        )


class UserDetailSerializer(BaseUserSerializer):

    class Meta(BaseUserSerializer.Meta):
        model = user
        fields = '__all__'


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        obj = self.user

        data.update({
            'id': obj.id,
            'email': obj.email,
            'username': obj.username,
            'is_active': obj.is_active
        })

        return data

