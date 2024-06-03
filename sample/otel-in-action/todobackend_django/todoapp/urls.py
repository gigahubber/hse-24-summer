from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.get_todos, name='get_todos'),
    path('todos/add/', views.add_todos, name='add_todos'),
    path('todos/delete/<str:todo>', views.remove_todos, name='remove_todos'),
]