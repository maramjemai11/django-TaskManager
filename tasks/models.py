from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from .constants import TaskStatus, TaskPriority

# Create your models here.

class Task(models.Model):
    """
    Represents a task belonging to a user.

    Attributes:
        title (str): The title of the task.
        description (str): Optional detailed description of the task.
        created_date (datetime): When the task was created.
        due_date (datetime): When the task is due.
        completed_date (datetime): When the task was completed.
        status (TaskStatus): The current status of the task.
        priority (TaskPriority): The priority level of the task.
        user (User): The user who owns the task.
    """
    title = models.CharField(
        max_length=200,
        verbose_name="Title",
        help_text="Enter a short title for the task."
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Description",
        help_text="Optional detailed description of the task."
    )
    created_date = models.DateTimeField(
        default=timezone.now,
        verbose_name="Created Date",
        help_text="The date and time when the task was created."
    )
    due_date = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name="Due Date",
        help_text="The date and time by which the task should be completed."
    )
    completed_date = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name="Completed Date",
        help_text="The date and time when the task was marked as completed."
    )
    status = models.CharField(
        max_length=20,
        choices=TaskStatus.choices(),
        default=TaskStatus.PENDING,
        verbose_name="Status",
        help_text="The current status of the task."
    )
    priority = models.CharField(
        max_length=10,
        choices=TaskPriority.choices(),
        default=TaskPriority.MEDIUM,
        verbose_name="Priority",
        help_text="The priority level of the task."
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tasks',
        verbose_name="User",
        help_text="The user who owns this task."
    )
    
    class Meta:
        ordering = ['-created_date']
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
    
    def __str__(self):
        """Return the string representation of the task (its title)."""
        return self.title
    
    @property
    def is_overdue(self):
        """
        Returns True if the task is overdue and not completed.
        Returns:
            bool: True if overdue, False otherwise.
        """
        if self.due_date and self.status != TaskStatus.COMPLETED:
            return timezone.now() > self.due_date
        return False
