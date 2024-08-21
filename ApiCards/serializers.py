from rest_framework import serializers

from .models import Card

class ApiCardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields= ['id','title','description','created_at','multiverseid']
        read_only = ['created_at',]