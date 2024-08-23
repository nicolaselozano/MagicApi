from rest_framework import serializers

from .Models.models import Card
from .Models.User import User

class ApiCardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields= ['id','title','description','created_at','multiverseid']
        read_only = ['created_at',]

class ApiCardsSerializerUser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= ['id','name','email','authId']
        read_only = ['created_at',]