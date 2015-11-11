from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from django.views.generic import View
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from todo.models import ToDo
from api.serializers import ToDoSerializer
# Create your views here.


#GET/POST VIEW (/api/ToDos/)



@api_view(['GET', 'POST'])
def list_create_todos(request):

    if request.method == "GET":
        ToDos = ToDo.objects.all()
        serializer = ToDoSerializer(ToDos, many=True)

        return Response(serializer.data)

    elif request.method == "POST":
        serializer = ToDoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#UPDATE/DELETE VIEW (/api/ToDos/{id}
class DetailUpdateTodo(APIView):

    def get(self, request, pk, format=None):
       
        todo = get_object_or_404(ToDo, pk=pk)
        serializer = ToDoSerializer(todo)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        todo = get_object_or_404(ToDo, pk=pk)
        serializer = ToDoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        todo = get_object_or_404(ToDo, pk=pk)
        todo.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)