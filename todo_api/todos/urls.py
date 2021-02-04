from django.urls import path, include
from . import views

urlpatterns = [
    path('todos/', views.ToDoList.as_view(), name='todo_list'),
    path('todos/<int:pk>', views.ToDoDetail.as_view(), name='todo_detail')
]
