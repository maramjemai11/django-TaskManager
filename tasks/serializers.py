from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User
from .constants import TaskStatus, TaskPriority


class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.
    """
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        """
        Create a new user with the provided validated data.
        """
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email', '')
        )
        return user

class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for Task model.
    """
    status = serializers.ChoiceField(choices=TaskStatus.choices())
    priority = serializers.ChoiceField(choices=TaskPriority.choices())
    title = serializers.CharField(max_length=200, min_length=1)

    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'created_date', 'due_date',
            'completed_date', 'status', 'priority', 'user'
        ]
        read_only_fields = ['id', 'created_date', 'completed_date', 'user']


class TaskFilterSerializer(serializers.Serializer):
    """
    Serializer for filtering and sorting tasks.
    """
    status = serializers.ChoiceField(choices=[choice[0] for choice in TaskStatus.choices()], required=False)
    sort = serializers.ChoiceField(choices=[
        'title', '-title', 'due_date', '-due_date', 
        'priority', '-priority', 'created_date', '-created_date'
    ], required=False, default='-created_date')