# Generated by Django 4.1.3 on 2024-08-31 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Feedback",
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
                ("stars", models.IntegerField()),
                ("comment", models.TextField()),
                (
                    "images",
                    models.ImageField(
                        blank=True, null=True, upload_to="feedback_images/"
                    ),
                ),
                (
                    "category",
                    models.CharField(
                        blank=True,
                        choices=[("positive", "Positive"), ("negative", "Negative")],
                        max_length=8,
                    ),
                ),
            ],
        ),
    ]
