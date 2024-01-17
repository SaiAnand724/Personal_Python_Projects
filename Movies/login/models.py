from django.db import models

# Create your models here.
class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length = 200)
    age = models.IntegerField()