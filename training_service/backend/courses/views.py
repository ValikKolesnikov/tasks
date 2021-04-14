from django.db import IntegrityError
from rest_framework import status, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

import courses.serializers as serializers
from courses.services import test_service, reading_material_service
from .models import Course, Participation, Test, ReadingMaterial, CourseProgress, ReadingMaterialProgress, TestProgress
from .pagination import CourseListPagination
from .services import participation_service, test_service


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

    @action(methods=['get'], detail=True)
    def class_room(self, request, pk):
        course = self.get_object()
        user = request.user
        participation = get_object_or_404(
            queryset=Participation.objects.prefetch_related('user', 'course').all(),
            user=user,
            course=course
        )
        course = participation.course
        course_data = {
            'tasks': course.tasks,
            'course': course
        }
        serializer = serializers.CourseClassRoomSerializer(course_data, context={'participation': participation})
        return Response(data=serializer.data)


class ReadingMaterialViewSet(viewsets.GenericViewSet):
    queryset = ReadingMaterial.objects.all()

    @action(methods=['post'], detail=True)
    def complete(self, request, pk):
        reading_material = self.get_object()
        reading_material_service.set_complete(reading_material=reading_material,
                                              user=request.user)
        return Response(status=status.HTTP_200_OK)


class TestViewSet(viewsets.GenericViewSet):
    queryset = Test.objects.all()

    @action(methods=['post'], detail=True)
    def complete(self, request, pk):
        test = self.get_object()
        test_service.set_complete(test=test,
                                  user=request.user)
        return Response(status=status.HTTP_200_OK)

    @action(methods=['post'], detail=True)
    def check_answer(self, request, pk):
        test = self.get_object()
        is_right = test_service.is_answer_right(test, request.data.get('answers'))
        return Response(data={'is_right': is_right})
