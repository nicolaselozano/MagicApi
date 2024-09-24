from django.db import models

class user(models.Model):
    USER_TYPE_CHOICES = (
        (1,'Admin'),
        (2,'User'),
    )
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    authId = models.CharField(max_length=100)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)

def __str__(self):
    return self.name
