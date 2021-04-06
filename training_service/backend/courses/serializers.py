from rest_framework import serializers
from . import models
from rest_polymorphic.serializers import PolymorphicSerializer


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


class CourseSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True)

    class Meta:
        model = models.Course
        fields = ['id', 'name', 'description', 'tasks']


class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = ['id', 'name', 'description']
