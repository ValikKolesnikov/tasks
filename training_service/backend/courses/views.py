from rest_framework import status, viewsets, mixins
from .pagination import CourseListPagination
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User, Group
import courses.serializers as serializers
from .models import Course, ReadingMaterial


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = serializers.CourseListSerializer
    pagination_class = CourseListPagination
