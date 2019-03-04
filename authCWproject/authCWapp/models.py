from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class FitnessModel(models.Model):
    username = models.CharField(max_length=50)
    calories = models.IntegerField()
    date = models.DateField(default="")
    userTableForeignKey = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.username
