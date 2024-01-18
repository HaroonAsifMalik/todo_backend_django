from django.urls import path , include
from .views import  ListTodo , DetailTodo

urlpatterns = [
    path('', ListTodo.as_view() , name='home'),
    path('<int:pk>/', DetailTodo.as_view(), name='detail')
]