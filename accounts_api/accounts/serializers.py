from rest_framework import serializers
from django.contrib.auth.models import User, Group
from rest_framework.generics import get_object_or_404
import accounts.services.user_service as user_service
import accounts.services.token_service as token_service
import jwt


class PasswordResetSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_old_password(self, old_password):
        user = get_object_or_404(queryset=User.objects.all(), id=self.initial_data.get('user_id'))
        if not user.check_password(self.initial_data.get('old_password')):
            raise serializers.ValidationError('Wrong password')


class GroupUserCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.update({'user_count': self.context.get('user_counts').get(instance.id)})
        return data


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name', 'permissions')


class UserRequestSerializer(serializers.ModelSerializer):
    groups = serializers.PrimaryKeyRelatedField(many=True, queryset=Group.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'groups')

    def create(self, validated_data):
        username, email, password, groups = validated_data.values()
        user = user_service.create(username=username,
                                   email=email,
                                   password=password,
                                   groups=groups)
        return user

    def update(self, instance, validated_data):
        username = validated_data.get('username')
        email = validated_data.get('email')
        groups = validated_data.get('groups')
        user = user_service.update(user=instance,
                                   username=username,
                                   email=email,
                                   groups=groups)
        return user


class UserResponseSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'groups')


class TokenResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.update({'token': self.context.get('token')})
        return data


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
