from rest_framework import status, viewsets, mixins
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User, Group
import accounts.serializers as serializers


class UserViewSet(mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = serializers.UserRequestSerializer
    queryset = User.objects.prefetch_related('groups').all()

    def create(self, request, *args, **kwargs):
        request_serializer = self.serializer_class(data=request.data)
        request_serializer.is_valid(raise_exception=True)
        user = request_serializer.save()
        response_serializer = serializers.UserResponseSerializer(user)
        return Response(data=response_serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = serializers.UserResponseSerializer(user)
        return Response(data=serializer.data)

    def partial_update(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.serializer_class(instance=user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        response_serializer = serializers.UserResponseSerializer(user)
        return Response(data=response_serializer.data)

    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=['patch'], detail=True)
    def reset_password(self, request):
        user = self.get_object()
        serializer = serializers.PasswordResetSerializer(data=request.data, context={'user': user})
        serializer.is_valid(raise_exception=True)
        user.set_password(serializer.validated_data.get('new_password'))
        user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=['get'], detail=False)
    def current(self, request):
        current_user = request.user
        serializer = serializers.UserResponseSerializer(current_user)
        return Response(data=serializer.data)


class GroupViewSet(mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    serializer_class = serializers.GroupSerializer
    queryset = Group.objects.prefetch_related('permissions').all()


class TokenViewSet(viewsets.GenericViewSet):
    @action(methods=['post'], detail=False)
    def obtain(self, request):
        token_serializer = serializers.ObtainTokenSerializer(data=request.data)
        token_serializer.is_valid(raise_exception=True)
        data = {
            'user': token_serializer.validated_data.get('user'),
            'token': token_serializer.validated_data.get('token')
        }
        response_serializer = serializers.TokenResponseSerializer(data)
        return Response(data=response_serializer.data)

    @action(methods=['post'], detail=False)
    def verify(self, request):
        verify_serializer = serializers.VerifyTokenSerializer(data=request.data)
        verify_serializer.is_valid(raise_exception=True)
        user = verify_serializer.validated_data.get('user')
        token = verify_serializer.validated_data.get('token')
        response_serializer = serializers.TokenResponseSerializer(user, context={'token': token})
        return Response(data=response_serializer.data)
