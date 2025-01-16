from django.urls import path
from . import views

urlpatterns = [
    path('', views.kanban_board, name='kanban_board'),
    path('add/', views.add_task, name='add_task'),
    path('update_task_status/', views.update_task_status, name='update_task_status'), 
     path('delete_task/', views.delete_task, name='delete_task'),
]
