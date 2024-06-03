from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer
import logging

# Log in console
logger = logging.getLogger(__name__)

# Create your views here.
@api_view(['GET'])
def get_todos(request):
    try:
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        logger.info('GET /todos/ ' + str(serializer.data))
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Todo.DoesNotExist:
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def add_todo(request):
    serializer = TodoSerializer(data={'todo': request.data.get('todo')})
    try:
        serializer.save()
        logger.info('POST /todos/ ' + str(serializer.data))
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Todo.DoesNotExist:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def remove_todo(request, todo):
    try:
        todo_instance = Todo.objects.get(todo=todo)
        todo_instance.delete()
        logger.info("DELETE /todos/ " + todo)
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Todo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)