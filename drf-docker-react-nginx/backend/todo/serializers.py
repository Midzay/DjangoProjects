from rest_framework import serializers
from .models import MatrixTodo

class MatrixTodoSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = MatrixTodo
        fields = ('id','title','completed','class_task')
