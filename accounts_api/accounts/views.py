from django.db.models import Count
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User, Group
import accounts.serializers as serializers
import rest_framework.serializers as rest_serializers
from rest_framework import generics
from datetime import datetime
from django_filters import rest_framework as filters
from accounts.services import user_service


class UserList(generics.GenericAPIView):
    serializer_class = serializers.UserRequestSerializer
    queryset = User.objects.prefetch_related('groups', 'groups__permissions').all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = user_service.UserGroupFilter

    def get(self, request):
        users = self.filter_queryset(self.queryset)
        serializer = serializers.UserResponseSerializer(users, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        request_serializer = serializers.UserRequestSerializer(data=request.data)
        request_serializer.is_valid(raise_exception=True)
        user = request_serializer.save()
        response_serializer = serializers.UserResponseSerializer(user)
        return Response(data=response_serializer.data, status=status.HTTP_201_CREATED)


class UserDetail(APIView):
    def get(self, request, id):
        user = get_object_or_404(queryset=User.objects.all(), id=id)
        serializer = serializers.UserResponseSerializer(user)
        return Response(data=serializer.data)

    def patch(self, request, id):
        user = get_object_or_404(queryset=User.objects.all(), id=id)
        serializer = serializers.UserRequestSerializer(instance=user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        response_serializer = serializers.UserResponseSerializer(user)
        return Response(data=response_serializer.data)

    def delete(self, request, id):
        user = get_object_or_404(queryset=User.objects.all(), id=id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GroupList(APIView):
    def get(self, request):
        groups = Group.objects.all()
        serializer = serializers.GroupSerializer(groups, many=True)
        return Response(data=serializer.data)


class CurrentUserDetail(APIView):
    def get(self, request):
        current_user = request.user
        serializer = serializers.UserResponseSerializer(current_user)
        return Response(data=serializer.data)


class PasswordReset(APIView):
    def patch(self, request, id):
        user = get_object_or_404(queryset=User.objects.all(), id=id)
        serializer = serializers.PasswordResetSerializer(data=request.data, context={'user': user})
        serializer.is_valid(raise_exception=True)
        user.set_password(serializer.validated_data.get('new_password'))
        user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserCount(APIView):
    def get(self, request):
        if request.query_params.get('only_admin').lower() == 'true':
            users = User.objects.filter(is_superuser=True)
            return Response(data={'admin_count': users.count()})
        elif request.query_params.get('only_active').lower() == 'true':
            users = User.objects.filter(is_active=True)
            return Response(data={'active_count': users.count()})
        else:
            return Response(data={'users_count': User.objects.count()})


class UserRegisteredCount(APIView):
    def get(self, request):
        now = datetime.now()
        if request.query_params.get('time_interval') == 'month':
            users = User.objects.filter(date_joined__month=now.month)
            return Response(data={'in_month': users.count()})
        elif request.query_params.get('time_interval') == 'week':
            users = User.objects.filter(date_joined__week=now.strftime("%V"))
            return Response(data={'in_week': users.count()})
        return Response(status=status.HTTP_400_BAD_REQUEST)


class UserGroups(APIView):
    def get(self, request):
        groups = Group.objects.filter(user__isnull=False).distinct()
        group_ids = groups.values_list('id', flat=True)
        return Response(data=group_ids)


class GroupUsersCount(APIView):
    def get(self, request):
        groups = Group.objects.all().annotate(user_count=Count('user'))
        serializer = serializers.GroupUserCountSerializer(groups, many=True)
        return Response(data=serializer.data)


class ObtainToken(APIView):
    def post(self, request):
        token_serializer = serializers.ObtainTokenSerializer(data=request.data)
        token_serializer.is_valid(raise_exception=True)
        data = {
            'user': token_serializer.validated_data.get('user'),
            'token': token_serializer.validated_data.get('token')
        }
        response_serializer = serializers.TokenResponseSerializer(data)
        return Response(data=response_serializer.data)


class VerifyToken(APIView):
    def post(self, request):
        verify_serializer = serializers.VerifyTokenSerializer(data=request.data)
        verify_serializer.is_valid(raise_exception=True)
        user = verify_serializer.validated_data.get('user')
        token = verify_serializer.validated_data.get('token')
        response_serializer = serializers.TokenResponseSerializer(user, context={'token': token})
        return Response(data=response_serializer.data)
