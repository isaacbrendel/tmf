# tasks/models.py

from django.db import models
from backend.employees.models import Employee

class Task(models.Model):
    TO_DO = 'To Do'
    IN_PROGRESS = 'In Progress'
    COMPLETED = 'Completed'
    
    STATUS_CHOICES = [
        (TO_DO, 'To Do'),
        (IN_PROGRESS, 'In Progress'),
        (COMPLETED, 'Completed'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=TO_DO  # Set 'To Do' as the default status
    )
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    assigned_to = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.get_status_display()}"
