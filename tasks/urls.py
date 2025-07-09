"""
URL patterns for the tasks app.
Includes task CRUD, status toggle, and registration endpoints.
"""
from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    # Task list and creation
    path('', views.task_list, name='task_list'),
    path('create/', views.task_create, name='task_create'),

    # Task detail, update, delete
    path('<int:pk>/', views.task_detail, name='task_detail'),
    path('<int:pk>/edit/', views.task_update, name='task_update'),
    path('<int:pk>/delete/', views.task_delete, name='task_delete'),

    # Task status toggle
    path('<int:pk>/toggle/', views.task_toggle_complete, name='task_toggle_complete'),

    # User registration (API view)
    path('register/', views.RegisterView.as_view(), name='register'),
    
] 