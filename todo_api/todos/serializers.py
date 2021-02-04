from rest_framework import serializers
from .services import ToDoService, CategoryService, TagService


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=300)


class TagSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=300)


class ToDoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    text = serializers.CharField(max_length=300)
    category = CategorySerializer(allow_null=True)
    tags = TagSerializer(many=True)

    def create(self, validated_data):
        data = ToDoService.get_data_from_validation(self, validated_data)
        todo = ToDoService.create(text=data['text'], category=data['category'], tags=data['tags'])
        return todo

    def update(self, instance, validated_data):
        data = ToDoService.get_data_from_validation(self, validated_data)
        todo = ToDoService.update(instance, text=data['text'], category=data['category'], tags=data['tags'])
        return todo
