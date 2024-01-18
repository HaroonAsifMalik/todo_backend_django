from django.shortcuts import render
from rest_framework import generics
from .serializers import TodoSerializer
from .models import Todo

# Create your views here.

class ListTodo(generics.ListAPIView):  # Corrected the typo: ListAPIView
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class DetailTodo(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
