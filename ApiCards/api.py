from .models.card import card
from .models.user import user
from .models.abilities import abilities
from rest_framework import viewsets,permissions
from .serializer.cards import ApiCardsSerializer
from .serializer.users import UserSerializer
from .serializer.abilities import AbilitiesSerializar

class ApiCardsViewSet(viewsets.ModelViewSet):
    queryset = card.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = ApiCardsSerializer

class ApiUserViewSet(viewsets.ModelViewSet):
    queryset = user.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = UserSerializer

class ApiAbilitiesViewSet(viewsets.ModelViewSet):
    queryset = abilities.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = AbilitiesSerializar