from django.shortcuts import render
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User, Group
from .serializers import UserSerializer, GroupSerializer, PasswordResetSerializer
from datetime import datetime
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer


class UserList(APIView):
    def get(self, request):
        groups = []
        groups_str = request.query_params.get('groups')
        if groups_str:
            groups = [Group.objects.filter(name=group_name).first() for group_name in groups_str.split(',')]
            users = User.objects.filter(groups__in=groups)
        else:
            users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        s = UserSerializer(User(username="asdf", password='123'))
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class UserDetail(APIView):
    def get(self, request, id):
        user = get_object_or_404(queryset=User.objects.all(), id=id)
        serializer = UserSerializer(user)
        return Response(data=serializer.data)

    def patch(self, request, id):
        user = get_object_or_404(queryset=User.objects.all(), id=id)
        serializer = UserSerializer(instance=user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)


class GroupList(APIView):
    def get(self, request):
        groups = Group.objects.all()
        serializer = GroupSerializer(groups, many=True)
        return Response(data=serializer.data)


class CurrentUserDetail(APIView):
    def get(self, request):
        current_user = request.user
        serializer = UserSerializer(current_user)
        return Response(data=serializer.data)


class PasswordReset(APIView):
    def get(self, request, id):
        user = get_object_or_404(queryset=User.objects.all(), id=id)
        serializer = UserSerializer(instance=user)
        return Response(data=serializer.data)

    def patch(self, request, id):
        user = get_object_or_404(queryset=User.objects.all(), id=id)
        serializer = PasswordResetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if not user.check_password(serializer.data.get('old_password')):
            return Response(data={'old_password': 'Wrong password'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            user.set_password(serializer.data.get('new_password'))
            user.save()
            return Response(status=status.HTTP_204_NO_CONTENT)


class UserCount(APIView):
    def get(self, request):
        if request.query_params.get('only_admin') == 'True':
            users = [user for user in User.objects.all() if user.is_superuser]
            return Response(data={'admin_count': len(users)})
        elif request.query_params.get('only_active') == 'True':
            users = [user for user in User.objects.all() if user.is_active]
            return Response(data={'active_count': len(users)})
        else:
            return Response(data={'users_count': len(User.objects.all())})


class UserRegisteredCount(APIView):
    def get(self, request):
        now = datetime.now()
        if request.query_params.get('time_interval') == 'month':
            users = [user for user in User.objects.all() if
                     user.date_joined.month == now.month]
            return Response(data={'month_interval': len(users)})
        elif request.query_params.get('time_interval') == 'week':
            users = [user for user in User.objects.all() if
                     datetime.date(user.date_joined).strftime("%V") == now.strftime("%V")]
            return Response(data={'week_interval': len(users)})
        return Response(status=status.HTTP_400_BAD_REQUEST)


class UserGroups(APIView):
    def get(self, request):
        group_ids = [group.id for group in Group.objects.all() if group.user_set]
        return Response(data=group_ids)


class GroupUsersCount(APIView):
    def get(self, request):
        data = [{'id': group.id,
                 'user_count': group.user_set.count()}
                for group in Group.objects.all()]
        return Response(data=data)


class ObtainToken(APIView):
    def get(self, request):
        return Response()

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = get_object_or_404(queryset=User.objects.all(), username=username)
        if user.check_password(password):
            token = Token.objects.get_or_create(user=user)[0]
            data = {
                'token': token.key
            }
            data.update(UserSerializer(user).data)
            return Response(data=data)
        return Response(data={'detail': 'Wrong password!'})


class VerifyToken(APIView):
    def get(self, request):
        return Response()

    def post(self, request):
        if Token.objects.get(user=request.user).key == request.data.get('token'):
            data = {
                'token': request.data.get('token')
            }
            data.update(UserSerializer(request.user).data)
            return Response(data=data)
        else:
            return Response(data={'token': 'Wrong token'})
