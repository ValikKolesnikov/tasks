from django.db import IntegrityError
from rest_framework import status, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

import courses.serializers as serializers
from .models import Course
from .pagination import CourseListPagination
from .services import participation_service


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
