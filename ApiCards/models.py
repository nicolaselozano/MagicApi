from django.db import models

# Create your models here.
class Card(models.Model):
    title = models.CharField(max_length=150)
    description : str = models.CharField(max_length=600)
    multiverseid : str = models.IntegerField(max_length=60)
    created_at : int = models.DateTimeField(auto_now_add=True)