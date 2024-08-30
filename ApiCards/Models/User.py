from django.db import models

class user(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    authId = models.CharField(max_length=100)

