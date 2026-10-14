from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):
    full_name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.full_name