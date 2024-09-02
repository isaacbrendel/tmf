# assets/models.py

from django.db import models

class Asset(models.Model):
    CATEGORY_CHOICES = [
        ('Vehicles', 'Vehicles'),
        ('Tools & Equipment', 'Tools & Equipment'),
        ('Riding Gear', 'Riding Gear'),
        ('Stable Equipment', 'Stable Equipment'),
        ('Medical Supplies', 'Medical Supplies'),
        ('Tech & Monitoring', 'Tech & Monitoring'),
        ('Safety Gear', 'Safety Gear'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        blank=True,  # Allow this field to be left blank
        null=True
    )
    description = models.TextField(blank=True, null=True)  # Optional description for AI training
    serial_number = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=20, default='Available')
    condition = models.TextField(blank=True, null=True)
    purchase_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.category if self.category else 'Uncategorized'}) - {self.status}"
