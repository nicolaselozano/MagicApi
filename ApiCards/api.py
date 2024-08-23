from .Models.models import Card
from .Models.User import User
from rest_framework import viewsets,permissions
from .serializers import ApiCardsSerializer,ApiCardsSerializerUser

class ApiCardsViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = ApiCardsSerializer

class ApiUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permissions_classes = [permissions.AllowAny]
    serializer_class = ApiCardsSerializerUser