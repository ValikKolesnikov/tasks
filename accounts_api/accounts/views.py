from django.db.models import Count
from django.shortcuts import render
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User, Group
from accounts.services import user_service
import accounts.serializers as serializers
from datetime import datetime
from rest_framework_jwt


class UserList(APIView):
    def get(self, request):
        groups = []
        groups_str = request.query_params.get('groups')
        if groups_str:
            users = User.objects.prefetch_related('groups', 'groups__permissions').filter(
                groups__name__in=groups_str.split(','))
        else:
            users = User.objects.prefetch_related('groups', 'groups__permissions').all()
        serializer = serializers.UserResponseSerializer(users, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        request_serializer = serializers.UserRequestSerializer(data=request.data)
        response_data = user_service.get_response_data(request_serializer=request_serializer)
        response_serializer = serializers.UserResponseSerializer(data=response_data)
        response_serializer.is_valid(raise_exception=True)
        request_serializer.save()
        return Response(data=response_serializer.data, status=status.HTTP_201_CREATED)


class UserDetail(APIView):
    def get(self, request, id):
        user = get_object_or_404(queryset=User.objects.all(), id=id)
        serializer = serializers.UserResponseSerializer(user)
        return Response(data=serializer.data)

    def patch(self, request, id):
        user = get_object_or_404(queryset=User.objects.all(), id=id)
        serializer = serializers.UserResponseSerializer(instance=user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)


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
        request.data.update({'user_id': id})
        serializer = serializers.PasswordResetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user.set_password(serializer.data.get('new_password'))
        user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserCount(APIView):
    def get(self, request):
        if request.query_params.get('only_admin') == 'True':
            users = User.objects.filter(is_superuser=True)
            return Response(data={'admin_count': users.count()})
        elif request.query_params.get('only_active') == 'True':
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
        group_ids = [group.id for group in Group.objects.all() if group.user_set]
        return Response(data=group_ids)


class GroupUsersCount(APIView):
    def get(self, request):
        groups = Group.objects.prefetch_related('permissions').all().annotate(user_count=Count('user'))
        serializer = serializers.GroupUserCountSerializer(groups, many=True)
        return Response(data=serializer.data)


class ObtainToken(APIView):
    def get(self, request):
        return Response()

    def post(self, request):
        request_serializer = serializers.ObtainTokenSerializer(data=request.data)
        request_serializer.is_valid(raise_exception=True)

        # username = request.data.get('username')
        # password = request.data.get('password')
        # user = get_object_or_404(queryset=User.objects.all(), username=username)
        # if user.check_password(password):
        #     token = Token.objects.get_or_create(user=user)[0]
        #     data = {
        #         'token': token.key
        #     }
        #     data.update(UserResponseSerializer(user).data)
        #     return Response(data=data)
        # return Response(data={'detail': 'Wrong password!'})


class VerifyToken(APIView):
    def get(self, request):
        return Response()

    def post(self, request):
        if Token.objects.get(user=request.user).key == request.data.get('token'):
            data = {
                'token': request.data.get('token')
            }
            data.update(serializers.UserResponseSerializer(request.user).data)
            return Response(data=data)
        else:
            return Response(data={'token': 'Wrong token'})
