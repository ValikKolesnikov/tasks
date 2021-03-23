from rest_framework import serializers
from django.contrib.auth.models import User, Group, Permission
from rest_framework.generics import get_object_or_404
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
        user = user_service.create(**validated_data)
        return user

    def update(self, instance, validated_data):
        user = user_service.update(user=instance, **validated_data)
        return user


class UserResponseSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'groups')


class TokenResponseSerializer(serializers.Serializer):
    user = UserResponseSerializer()
    token = serializers.CharField()


class ObtainTokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise serializers.ValidationError('User with this username does not exist')
        if not user.check_password(password):
            raise serializers.ValidationError('Wrong password')

        token = token_service.get_user_token(user=user)
        return {'user': user,
                'token': token
                }


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
