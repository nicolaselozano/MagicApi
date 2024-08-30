from django.db import models
from .models import card

class abilities(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    card_fk = models.ForeignKey(card, on_delete=models.CASCADE)