from rest_framework import status, viewsets, mixins
from .pagination import CourseListPagination
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User, Group
import courses.serializers as serializers
from .models import Course, ReadingMaterial, Participation, Role
from accounts.permissions import IsAuth
from datetime import datetime


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.prefetch_related('tasks').all()
    serializer_class = serializers.CourseListSerializer
    pagination_class = CourseListPagination
    permission_classes = [IsAuth]

    @action(methods=['post'], detail=True)
    def participate(self, request, pk):
        course = self.get_object()
        user = request.user
        data = {
            'user': user.id,
            'course': course.id,
            'enroll_time': datetime.now(),
            'role': Role.STUDENT
        }
        data.update(request.data)
        participation_serializer = serializers.ParticipationRequestSerializer(data=data)
        participation_serializer.is_valid(raise_exception=True)
        participation = participation_serializer.save()
        response_serializer = serializers.ParticipationResponseSerializer(participation)
        return Response(data=response_serializer.data)

    def retrieve(self, request, *args, **kwargs):
        course = self.get_object()
        serializer = serializers.CourseSerializer(course)
        return Response(data=serializer.data)


class ParticipationViewSet(viewsets.GenericViewSet):
    queryset = Participation.objects.all()
    serializer_class = serializers.ParticipationResponseSerializer
