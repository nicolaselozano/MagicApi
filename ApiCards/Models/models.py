from django.db import models
from User import User
# Create your models here.
class Card(models.Model):
    title = models.CharField(max_length=150)
    description : str = models.CharField(max_length=600)
    multiverseid : str = models.IntegerField()
    created_at : int = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

