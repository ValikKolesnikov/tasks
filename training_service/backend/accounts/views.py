from django.contrib.auth.models import User, Group
from rest_framework import status, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView

import accounts.serializers as serializers
from courses.models import Participation
from courses.serializers import ParticipationResponseSerializer
from .permissions import CurrentUserOrAdminUser


class UserViewSet(viewsets.GenericViewSet):
    serializer_class = serializers.UserRequestSerializer
    queryset = User.objects.prefetch_related('groups').all()
    permission_classes = [CurrentUserOrAdminUser]

    def get_permissions(self):
        if self.action != 'teacher_create' or self.action != 'student_create':
            self.permission_classes = [CurrentUserOrAdminUser]
        return super().get_permissions()

    @action(methods=['post'], detail=False)
    def teacher_create(self, request, *args, **kwargs):
        data = {
            'group': Group.objects.get_or_create(name='Teacher')[0].id
        }
        data.update(request.data)
        request_serializer = self.serializer_class(data=data)
        request_serializer.is_valid(raise_exception=True)
        user = request_serializer.save()
        response_serializer = serializers.UserResponseSerializer(user)
        return Response(data=response_serializer.data, status=status.HTTP_201_CREATED)

    @action(methods=['post'], detail=False)
    def student_create(self, request, *args, **kwargs):
        data = {
            'group': Group.objects.get_or_create(name='Student')[0].id
        }
        data.update(request.data)
        request_serializer = self.serializer_class(data=data)
        request_serializer.is_valid(raise_exception=True)
        user = request_serializer.save()
        response_serializer = serializers.UserResponseSerializer(user)
        return Response(data=response_serializer.data, status=status.HTTP_201_CREATED)

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
    def reset_password(self, request, pk):
        user = self.get_object()
        serializer = serializers.PasswordResetSerializer(data=request.data, context={'user': user})
        serializer.is_valid(raise_exception=True)
        user.set_password(serializer.validated_data.get('new_password'))
        user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=['post'], detail=False)
    def current(self, request):
        current_user = request.user
        serializer = serializers.UserResponseSerializer(current_user)
        return Response(data=serializer.data)


class ParticipationViewSet(viewsets.GenericViewSet):
    queryset = Participation.objects.prefetch_related('course', 'user').all()
    serializer_class = ParticipationResponseSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

    def list(self, request, *args, **kwargs):
        participation_list = self.get_queryset()
        serializer = ParticipationResponseSerializer(participation_list, many=True)
        return Response(data=serializer.data)


class GroupViewSet(mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    serializer_class = serializers.GroupSerializer
    queryset = Group.objects.prefetch_related('permissions').all()
    pagination_class = None


class ObtainTokenView(TokenObtainPairView):
    serializer_class = serializers.TokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        token_serializer = self.serializer_class(data=request.data)
        token_serializer.is_valid(raise_exception=True)
        data = {
            'user': token_serializer.validated_data.get('user'),
            'refresh': token_serializer.validated_data.get('refresh'),
            'access': token_serializer.validated_data.get('access')
        }
        response_serializer = serializers.TokenResponseSerializer(data)
        return Response(data=response_serializer.data)


class VerifyTokenView(TokenVerifyView):
    serializer_class = serializers.VerifyTokenSerializer

    def post(self, request, *args, **kwargs):
        verify_serializer = self.serializer_class(data=request.data)
        verify_serializer.is_valid(raise_exception=True)
        data = {
            'user': verify_serializer.validated_data.get('user'),
            'access': verify_serializer.validated_data.get('token')
        }
        response_serializer = serializers.TokenResponseSerializer(data)
        return Response(data=response_serializer.data)
