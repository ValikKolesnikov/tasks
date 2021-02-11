from rest_framework import serializers
from django.contrib.auth.models import User, Group
import accounts.services.user_service as user_service


class PasswordResetSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


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


class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'groups')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        username, email, password, _ = validated_data.values()
        groups_data = self.initial_data['groups']
        user = user_service.create(username=username,
                                   email=email,
                                   password=password,
                                   groups_data=groups_data)
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
