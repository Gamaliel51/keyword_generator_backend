from django.db import models


# Create your models here.
class SavedData(models.Model):
    username = models.CharField(max_length=255)
    abstract = models.CharField(max_length=10000000)
    keywords = models.CharField(max_length=100000)

