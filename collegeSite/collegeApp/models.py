from django.db import models

# Create your models here.

class users(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    role = models.CharField(max_length=30)

class colleges(models.Model):
    name = models.CharField(max_length=75)
    year = models.IntegerField()
    location = models.CharField(max_length=30)
    courses = models.CharField(max_length=200)
    strength = models.IntegerField()
    admission = models.DateField()