from django.contrib.auth.models import User
from rest_framework import serializers
from rest_polymorphic.serializers import PolymorphicSerializer

from accounts.serializers import UserResponseSerializer
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
        model = models.Test
        fields = ['id', 'is_complete']


class TestResponseSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)
    progress = serializers.SerializerMethodField()

    class Meta:
        model = models.Test
        fields = ['id', 'name', 'position_number', 'questions', 'progress']

    def get_progress(self, obj):
        progress = models.TestProgress.objects.get(course_progress__participation_id=self.context['participation'],
                                                   test_id=obj.id)
        return {
            'is_complete': progress.is_complete
        }


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Test
        fields = ['id', 'name', 'position_number']


class ReadingMaterialProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ReadingMaterialProgress
        fields = ['id', 'is_complete']


class ReadingMaterialSerializer(serializers.ModelSerializer):
    progress = serializers.SerializerMethodField()

    class Meta:
        model = models.ReadingMaterial
        fields = ['id', 'title', 'text', 'position_number', 'progress']

    def get_progress(self, obj):
        progress = models.ReadingMaterialProgress.objects.get(
            course_progress__participation_id=self.context['participation'],
            reading_material_id=obj.id)
        return {
            'is_complete': progress.is_complete
        }


class TaskSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        models.ReadingMaterial: ReadingMaterialSerializer,
        models.Test: TestSerializer
    }


class CourseProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseProgress
        fields = ['is_complete', 'progress', 'completion_date']


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


class CourseDetailSerializer(serializers.ModelSerializer):
    tasks = TaskResponseSerializer(many=True)

    class Meta:
        model = models.Course
        fields = ['id', 'name', 'description', 'tasks']


class CourseShortSerializer(serializers.ModelSerializer):
    progress = serializers.SerializerMethodField()

    class Meta:
        model = models.Course
        fields = ['id', 'name', 'description', 'progress']

    def get_progress(self, obj):
        progress = models.CourseProgress.objects.get(participation_id=self.context['participation'])
        return {
            'is_complete': progress.is_complete(),
            'completion_date': progress.completion_date
        }


class CourseClassRoomSerializer(serializers.Serializer):
    tasks = TaskResponseSerializer(many=True)
    course = CourseShortSerializer()
