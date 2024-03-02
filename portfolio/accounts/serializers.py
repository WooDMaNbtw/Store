from django.contrib.auth.models import User
from rest_framework import serializers
from django.db.models import Q


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
        )


class UserCreateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False, allow_blank=True)
    email = serializers.EmailField(allow_blank=False)
    confirm_email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'confirm_email',
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

    def create(self, validated_data):
        username = validated_data.get('username')
        email = validated_data.get('email')
        password = validated_data.get('password')
        user_obj = User(
            username=username,
            email=email
        )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data

    def validate_confirm_email(self, confirm_email):
        data = self.get_initial()
        email1 = data.get('email')

        if email1 != confirm_email:
            raise serializers.ValidationError("Emails must match.")

        return confirm_email

    def validate(self, data):
        email = data.get('email')
        user_queryset = User.objects.filter(email=email)
        if user_queryset.exists():
            raise serializers.ValidationError("This user has already been registered.")
        return data


class UserLoginSerializer(serializers.ModelSerializer):
    token = serializers.CharField(allow_blank=True, read_only=True)
    username = serializers.CharField(required=False, allow_blank=True)
    email = serializers.EmailField(allow_blank=False)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password',
            'token'
        )
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': 'text'
                }
            }
        }

    def validate(self, data):
        email = data.get('email')
        username = data.get('username')
        password = data.get('password')
        if not email:
            raise serializers.ValidationError("User email is required to login.")
        user = User.objects.filter(
            Q(email=email) |
            Q(username=username)
        ).distinct()
        # user = user.exclude(email__isnull=email).exclude(email__iexact='')
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise serializers.ValidationError("This username or email is not valid.")

        if user_obj:
            if not user_obj.check_password(password):
                raise serializers.ValidationError("Incorrect credentials please try again.")

        data['token'] = "NEWEWESDSD"

        return data

