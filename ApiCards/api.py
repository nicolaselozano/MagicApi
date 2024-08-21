from .models import Card
from rest_framework import viewsets,permissions
from .serializers import ApiCardsSerializer

class ApiCardsViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = ApiCardsSerializer
