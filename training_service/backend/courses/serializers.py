from rest_framework import serializers
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


class CourseSerializer(serializers.ModelSerializer):
    reading_materials = ReadingMaterialSerializer(many=True)
    tests = TestSerializer(many=True)

    class Meta:
        model = models.Course
        fields = ['id', 'name', 'description', 'reading_materials', 'tests']


class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = ['id', 'name', 'description']
