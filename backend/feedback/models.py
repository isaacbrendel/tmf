# feedback/models.py

from django.db import models

class Feedback(models.Model):
    POSITIVE = 'positive'
    NEGATIVE = 'negative'
    REVIEW_CATEGORIES = [
        (POSITIVE, 'Positive'),
        (NEGATIVE, 'Negative'),
    ]

    stars = models.IntegerField()
    comment = models.TextField()
    images = models.ImageField(upload_to='feedback_images/', blank=True, null=True)
    category = models.CharField(max_length=8, choices=REVIEW_CATEGORIES, blank=True)

    def save(self, *args, **kwargs):
        if self.stars >= 4:
            self.category = self.POSITIVE
        else:
            self.category = self.NEGATIVE
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.stars} Stars - {self.category}"
