from django.db import models
from django.urls import reverse

# Create your models here.

class Expenses(models.Model):
    date = models.DateField()
    category = models.CharField(max_length=264)
    description = models.CharField(max_length=264)
    amount = models.PositiveIntegerField()

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse("expense:list")
