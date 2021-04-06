import django_filters
from django.contrib.auth.models import User


class UserGroupFilter(django_filters.FilterSet):
    group = django_filters.CharFilter(field_name='groups__name')

    class Meta:
        model = User
        fields = ['group']
