# Generated by Django 4.1.3 on 2024-09-02 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Asset",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                (
                    "category",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Vehicles", "Vehicles"),
                            ("Tools & Equipment", "Tools & Equipment"),
                            ("Riding Gear", "Riding Gear"),
                            ("Stable Equipment", "Stable Equipment"),
                            ("Medical Supplies", "Medical Supplies"),
                            ("Tech & Monitoring", "Tech & Monitoring"),
                            ("Safety Gear", "Safety Gear"),
                        ],
                        max_length=50,
                        null=True,
                    ),
                ),
                ("description", models.TextField(blank=True, null=True)),
                ("serial_number", models.CharField(max_length=100, unique=True)),
                ("location", models.CharField(blank=True, max_length=100, null=True)),
                ("status", models.CharField(default="Available", max_length=20)),
                ("condition", models.TextField(blank=True, null=True)),
                ("purchase_date", models.DateField(blank=True, null=True)),
            ],
        ),
    ]
