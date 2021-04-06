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


class CourseViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Course.objects.prefetch_related('tasks').all()
    serializer_class = serializers.CourseListSerializer
    pagination_class = CourseListPagination
    permission_classes = [IsAuthenticated]

    @action(methods=['post'], detail=True)
    def participate(self, request, pk):
        course = self.get_object()
        user = request.user
        data = participation_service.get_participation_data(user=user, course=course, is_teacher=False)
        participation_serializer = serializers.ParticipationRequestSerializer(data=data)
        participation_serializer.is_valid(raise_exception=True)
        participation = participation_serializer.save()
        response_serializer = serializers.ParticipationResponseSerializer(participation)
        return Response(data=response_serializer.data)

    def retrieve(self, request, *args, **kwargs):
        course = self.get_object()
        serializer = serializers.CourseSerializer(course)
        return Response(data=serializer.data)

    @action(methods=['post'], detail=True)
    def detail(self, request, pk):
        course = self.get_object()
