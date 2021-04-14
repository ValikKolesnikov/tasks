from django.contrib.auth.models import User
from rest_framework import serializers
from rest_polymorphic.serializers import PolymorphicSerializer

from accounts.serializers import UserResponseSerializer
from courses.services import progress_service
from . import models


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Answer
        fields = ['id', 'text']


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = models.Question
        fields = ['id', 'text', 'answers']


class TestProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TestProgress
        fields = ['is_complete']


class TestResponseSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)
    progress = serializers.SerializerMethodField()

    class Meta:
        model = models.Test
        fields = ['id', 'name', 'position_number', 'questions', 'progress']

    def get_progress(self, obj):
        progress = progress_service.get_test_progress_or_none(test_id=obj.id,
                                                              participation_id=self.context['participation'])
        if progress:
            return TestProgressSerializer(progress).data
        return None


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Test
        fields = ['id', 'name', 'position_number']


class ReadingMaterialProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ReadingMaterialProgress
        fields = ['is_complete']


class ReadingMaterialSerializer(serializers.ModelSerializer):
    progress = serializers.SerializerMethodField()

    class Meta:
        model = models.ReadingMaterial
        fields = ['id', 'title', 'text', 'position_number', 'progress']

    def get_progress(self, obj):
        progress = progress_service.get_reading_material_progress_or_none(reading_material_id=obj.id,
                                                                          participation_id=self.context[
                                                                              'participation'])
        if progress:
            return ReadingMaterialProgressSerializer(progress).data
        return None


class TaskSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        models.ReadingMaterial: ReadingMaterialSerializer,
        models.Test: TestSerializer
    }


class CourseProgressSerializer(serializers.ModelSerializer):
    value = serializers.FloatField()

    class Meta:
        model = models.CourseProgress
        fields = ['is_complete', 'completion_date', 'value']


class CourseSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True)

    class Meta:
        model = models.Course
        fields = ['id', 'name', 'description', 'tasks']


class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = ['id', 'name', 'description']


class ParticipationRequestSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.prefetch_related('groups').all())
    course = serializers.PrimaryKeyRelatedField(queryset=models.Course.objects.prefetch_related('tasks').all())

    class Meta:
        model = models.Participation
        fields = ['id', 'user', 'course', 'role', 'enroll_time']


class ParticipationResponseSerializer(serializers.ModelSerializer):
    user = UserResponseSerializer()
    course = CourseSerializer()

    class Meta:
        model = models.Participation
        fields = ['id', 'user', 'course', 'role', 'enroll_time']


class TaskResponseSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        models.ReadingMaterial: ReadingMaterialSerializer,
        models.Test: TestResponseSerializer
    }


class CourseShortSerializer(serializers.ModelSerializer):
    progress = serializers.SerializerMethodField()

    class Meta:
        model = models.Course
        fields = ['id', 'name', 'description', 'progress']

    def get_progress(self, obj):
        progress = progress_service.get_course_progress_or_none(participation_id=self.context['participation'])
        if progress:
            return CourseProgressSerializer(progress).data
        return None


class CourseClassRoomSerializer(serializers.Serializer):
    tasks = TaskResponseSerializer(many=True)
    course = CourseShortSerializer()
