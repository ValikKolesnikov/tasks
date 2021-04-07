from datetime import datetime

from rest_framework import serializers
from . import models
from rest_polymorphic.serializers import PolymorphicSerializer
from django.contrib.auth.models import User
from accounts.serializers import UserResponseSerializer


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Answer
        fields = ['id', 'text']


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = models.Question
        fields = ['id', 'text', 'answers']


class TestResponseSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = models.Test
        fields = ['id', 'name', 'position_number', 'questions']


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Test
        fields = ['id', 'name', 'position_number']


class ReadingMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ReadingMaterial
        fields = ['id', 'title', 'text', 'position_number']


class TaskSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        models.ReadingMaterial: ReadingMaterialSerializer,
        models.Test: TestSerializer
    }


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
