from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MatrixTodoSerialaizer
from .models import MatrixTodo

class MatrixTodoView(viewsets.ModelViewSet):
    serializer_class = MatrixTodoSerialaizer
    queryset = MatrixTodo.objects.all()


