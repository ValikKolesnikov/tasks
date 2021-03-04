from django.contrib.auth.models import User
import django_filters


def create(username, email, password, groups):
    user = User(username=username, email=email)
    user.set_password(password)
    user.save()
    user.groups.set(groups)
    return user


def update(user, username, email, groups):
    if username:
        user.username = username
    if email:
        user.email = email
    user.save()
    if groups:
        user.groups.set(groups)
    return user


class UserGroupFilter(django_filters.FilterSet):
    group = django_filters.CharFilter(field_name='groups__name')

    class Meta:
        model = User
        fields = ['group']