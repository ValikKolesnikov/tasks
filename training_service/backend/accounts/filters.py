from rest_framework import filters
from rest_framework.generics import get_object_or_404
from django.contrib.auth.models import User


class ParticipationListFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        user_id = request.query_params.get('user_id')
        user = get_object_or_404(queryset=User.objects.all(), id=user_id)
        return queryset.filter(user=user)
