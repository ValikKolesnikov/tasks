from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from todos.serializers import ToDoSerializer
import todos.services.todo as todo_service


class ToDoList(APIView):
    def get(self, request):
        todos = todo_service.get_all()
        serializer = ToDoSerializer(todos, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        serializer = ToDoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class ToDoDetail(APIView):
    def get(self, request, pk):
        todo = todo_service.get(pk=pk)
        serializer = ToDoSerializer(todo)
        return Response(data=serializer.data)

    def put(self, request, pk):
        todo = todo_service.get(pk=pk)
        serializer = ToDoSerializer(todo, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        todo_service.delete(pk=pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
