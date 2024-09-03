from rest_framework import serializers

from ..models.card import card,user
from .users import ApiCardsSerializerUser

class ApiCardsSerializer(serializers.ModelSerializer):
    user_details = ApiCardsSerializerUser(source='user', read_only=True)
    user = serializers.PrimaryKeyRelatedField(queryset=user.objects.all(), write_only=True)
    class Meta:
        model = card
        fields= ['id','title','description','created_at','multiverseid','user','user_details']
        read_only_fields = ['created_at', 'user_details']
