from rest_framework import routers
from ..api import ApiCardsViewSet,ApiUserViewSet,ApiAbilitiesViewSet
from ..views.views import UserManagerView
from django.urls import path, include

router = routers.DefaultRouter()

router.register(r'api/cards',ApiCardsViewSet,'cards')
router.register(r'api/users',ApiUserViewSet,'users')
router.register(r'api/abilities',ApiAbilitiesViewSet,'abilities')

urlpatterns = [
    path(r'api/user-manager/', UserManagerView.as_view(), name='user-manager'),
]

# Incluir las rutas registradas por el router
urlpatterns += router.urls