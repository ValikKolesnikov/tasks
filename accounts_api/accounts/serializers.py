from rest_framework import serializers
from django.contrib.auth.models import User, Group
from rest_framework.generics import get_object_or_404

import accounts.services.user_service as user_service


class PasswordResetSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_old_password(self, old_password):
        user = get_object_or_404(queryset=User.objects.all(), id=self.initial_data.get('user_id'))
        if not user.check_password(self.initial_data.get('old_password')):
            raise serializers.ValidationError('Wrong password')


class GroupUserCountSerializer(serializers.ModelSerializer):
    user_count = serializers.IntegerField()

    class Meta:
        model = Group
        fields = ('id', 'name', 'permissions', 'user_count')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name', 'permissions')
        extra_kwargs = {'name': {'validators': []}}


class UserRequestSerializer(serializers.ModelSerializer):
    groups = serializers.PrimaryKeyRelatedField(many=True, queryset=Group.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'groups')

    def create(self, validated_data):
        username, email, password, _ = validated_data.values()
        group_ids = self.initial_data['groups']
        user = user_service.create(username=username,
                                   email=email,
                                   password=password,
                                   group_ids=group_ids)
        return user

    def update(self, instance, validated_data):
        username = validated_data.get('username')
        email = validated_data.get('email')
        groups_data = self.initial_data.get('groups')
        user = user_service.update(user=instance,
                                   username=username,
                                   email=email,
                                   groups_data=groups_data)
        return user


class UserResponseSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'groups')
        extra_kwargs = {'password': {'write_only': True}}


class TokenResponseSerializer(serializers.ModelSerializer):
    token = serializers.CharField()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'groups')


class ObtainTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')

    def validate(self, attrs):
        username, password = attrs.values()
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise serializers.ValidationError('User with this username does not exist')
        if not user.check_password(password):
            raise serializers.ValidationError('Wrong password')


