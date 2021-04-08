from rest_framework import status, viewsets, mixins
from .pagination import CourseListPagination
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User, Group
import courses.serializers as serializers
from .models import Course, ReadingMaterial, Participation, Role
from datetime import datetime
from rest_framework.permissions import IsAuthenticated
from .services import participation_service
from django.forms.models import model_to_dict
from django.db import IntegrityError


class CourseViewSet(mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    queryset = Course.objects.prefetch_related('tasks').all()
    serializer_class = serializers.CourseListSerializer
    pagination_class = CourseListPagination
    permission_classes = [IsAuthenticated]

    @action(methods=['post'], detail=True)
    def enroll_as_student(self, request, pk):
        course = self.get_object()
        user = request.user
        participation = None
        try:
            participation = participation_service.enroll_as_student(user=user, course=course)
        except IntegrityError:
            return Response(data='You already enrolled in this course', status=status.HTTP_400_BAD_REQUEST)
        response_serializer = serializers.ParticipationResponseSerializer(participation)
        return Response(data=response_serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        course = self.get_object()
        serializer = serializers.CourseSerializer(course)
        return Response(data=serializer.data)
