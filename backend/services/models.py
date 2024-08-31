# services/models.py

from django.db import models

class HorseTransportation(models.Model):
    number_of_horses = models.IntegerField()
    date = models.DateField()
    distance = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)  # Optional description

    def __str__(self):
        return f"Transport on {self.date} for {self.number_of_horses} horses"

class HorseBoarding(models.Model):
    number_of_animals = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)  # Can be null for indefinite stay
    description = models.TextField(blank=True, null=True)  # Optional description

    def is_indefinite(self):
        return self.end_date is None

    def __str__(self):
        if self.is_indefinite():
            return f"Boarding {self.number_of_animals} animals starting {self.start_date} (Indefinite)"
        return f"Boarding {self.number_of_animals} animals from {self.start_date} to {self.end_date}"
