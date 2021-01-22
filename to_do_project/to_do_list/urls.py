from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page_view, name='main_page_view'),
    path('add/<str:category_name>', views.add_todo_view, name='add_todo_view'),
    path('delete/<int:id>', views.delete_todo_view, name='delete_todo_view'),
    path('edit/<int:id>', views.edit_todo_view, name='edit_todo_view'),
    path('categories/<str:category_name>', views.category_page_view, name='category_page_view'),
]
