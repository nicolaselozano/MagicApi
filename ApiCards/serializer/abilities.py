from rest_framework import serializers
from ..models.abilities import abilities,card
from .cards import ApiCardsSerializer

class AbilitiesSerializar(serializers.ModelSerializer):
    card_details = ApiCardsSerializer(read_only=True)
    card = serializers.PrimaryKeyRelatedField(queryset=card.objects.all(), write_only=True)

    class Meta:
        model = abilities
        fields = ['id','name','description','card','card_details']
        read_only_fields = ['created_at', 'card_details']