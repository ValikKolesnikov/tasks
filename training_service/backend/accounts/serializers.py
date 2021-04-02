from rest_framework import serializers
from django.contrib.auth.models import User, Group, Permission
from rest_framework_simplejwt.serializers import TokenObtainSerializer
from rest_framework_simplejwt.tokens import RefreshToken

import accounts.services.user_service as user_service
import accounts.services.token_service as token_service
import jwt


class PasswordResetSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_old_password(self, old_password):
        if not self.context.get('user').check_password(old_password):
            raise serializers.ValidationError('Wrong password')


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ('id', 'name')


class GroupSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(many=True)

    class Meta:
        model = Group
        fields = ('id', 'name', 'permissions')


class UserRequestSerializer(serializers.ModelSerializer):
    groups = serializers.PrimaryKeyRelatedField(many=True, queryset=Group.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password', 'groups')

    def create(self, validated_data):
        user = user_service.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        user = user_service.update_user(user=instance, **validated_data)
        return user


class UserResponseSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'groups')


class TokenResponseSerializer(serializers.Serializer):
    user = UserResponseSerializer()
    refresh = serializers.CharField()
    access = serializers.CharField()


class TokenObtainPairSerializer(TokenObtainSerializer):
    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['user'] = self.user

        return data


class VerifyTokenSerializer(serializers.Serializer):
    token = serializers.CharField()

    def validate(self, attrs):
        token = attrs.get('token')
        try:
            user = token_service.decode_token(token=token)
        except jwt.DecodeError as error:
            raise serializers.ValidationError(error)
        return {
            'token': token,
            'user': user
        }
