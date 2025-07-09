"""
API URL patterns for the tasks app.
Includes DRF viewset router and explicit registration endpoint.
"""
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, RegisterView
from django.urls import path

# Router-based endpoints (CRUD for tasks)
router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = router.urls

# Explicit API endpoints
urlpatterns += [
    path('register/', RegisterView.as_view(), name='api_register'),
]
