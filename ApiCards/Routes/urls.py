from rest_framework import routers
from ..api import ApiCardsViewSet,ApiUserViewSet,ApiAbilitiesViewSet

router = routers.DefaultRouter()

router.register(r'api/cards',ApiCardsViewSet,'cards')
router.register(r'api/users',ApiUserViewSet,'users')
router.register(r'api/abilities',ApiAbilitiesViewSet,'abilities')

urlpatterns = router.urls