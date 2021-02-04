from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from todos.serializers import ToDoSerializer
from todos.services import ToDoService


class ToDoList(APIView):
    def get(self, request):
        todos = ToDoService.get_all()
        serializer = ToDoSerializer(todos, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        serializer = ToDoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ToDoDetail(APIView):
    def get(self, request, pk):
        todo = ToDoService.get(pk=pk)
        serializer = ToDoSerializer(todo)
        return Response(data=serializer.data)

    def put(self, request, pk):
        todo = ToDoService.get(pk=pk)
        serializer = ToDoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        ToDoService.delete(pk=pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
