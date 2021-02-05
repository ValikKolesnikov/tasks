from rest_framework import serializers
import todos.services.todo as todo_service


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
        data = todo_service.get_data_from_validation(self, validated_data)
        todo = todo_service.create(text=data['text'], category=data['category'], tags=data['tags'])
        return todo

    def update(self, instance, validated_data):
        data = todo_service.get_data_from_validation(self, validated_data)
        todo = todo_service.update(instance, text=data['text'], category=data['category'], tags=data['tags'])
        return todo
