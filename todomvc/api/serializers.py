from django.contrib.auth.admin import User
from rest_framework import serializers
from todo.models import ToDo

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'todo_set')


class ToDoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ToDo
        fields = ('id', 'title', 'completed', 'order')
