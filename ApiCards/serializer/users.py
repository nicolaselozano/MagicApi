from rest_framework import serializers
from ..models.user import user

class ApiCardsSerializerUser(serializers.ModelSerializer):
    class Meta:
        model = user
        fields= ['id','name','email','authId']
        read_only = ['created_at',]