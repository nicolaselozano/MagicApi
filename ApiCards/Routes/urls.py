from rest_framework import routers
from ..api import ApiCardsViewSet,ApiUserViewSet

router = routers.DefaultRouter()

router.register('api/cards',ApiCardsViewSet,'cards')
router.register('api/users',ApiUserViewSet,'users')

urlpatterns = router.urls