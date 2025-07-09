from django import forms
from .models import Task
from django.contrib.auth.models import User
from .constants import TaskStatus, TaskPriority

class TaskForm(forms.ModelForm):
    """
    Form for creating and updating Task instances.
    """
    title = forms.CharField(
        max_length=200,
        min_length=1,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter task title'
        }),
        label="Title",
        help_text="Enter a short title for the task."
    )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 4,
            'placeholder': 'Enter task description (optional)'
        }),
        label="Description",
        help_text="Optional detailed description of the task."
    )
    due_date = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control',
            'type': 'datetime-local'
        }),
        label="Due Date",
        help_text="The date and time by which the task should be completed."
    )
    status = forms.ChoiceField(
        choices=TaskStatus.choices(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Status",
        help_text="The current status of the task."
    )
    priority = forms.ChoiceField(
        choices=TaskPriority.choices(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Priority",
        help_text="The priority level of the task."
    )

    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'status', 'priority']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make due_date optional
        self.fields['due_date'].required = False 

class UserRegisterForm(forms.ModelForm):
    """
    Form for registering a new user.
    """
    password = forms.CharField(
        widget=forms.PasswordInput,
        min_length=8,
        label="Password",
        help_text="Password must be at least 8 characters long."
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password'] 