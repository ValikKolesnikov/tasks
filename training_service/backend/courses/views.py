from rest_framework import status, viewsets, mixins
from .pagination import CourseListPagination
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User, Group
import courses.serializers as serializers
from .models import Course, ReadingMaterial, Participation
from accounts.permissions import IsAuth


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = serializers.CourseListSerializer
    pagination_class = CourseListPagination
    permission_classes = [IsAuth]

    @action(methods=['post'], detail=True)
    def participate(self, request, pk):
        course = self.get_object()
        user = request.user
        data = {
            'user': user.id,
            'course': course.id
        }
        data.update(request.data)
        participation_serializer = serializers.ParticipationRequestSerializer(data=data)
        participation_serializer.is_valid(raise_exception=True)
        participation = participation_serializer.save()
        response_serializer = serializers.ParticipationResponseSerializer(participation)
        return Response(data=response_serializer.data)


class ParticipationViewSet(viewsets.GenericViewSet):
    queryset = Participation.objects.all()
    serializer_class = serializers.ParticipationResponseSerializer
