from rest_framework import routers
from ..api import ApiCardsViewSet

router = routers.DefaultRouter()

router.register('api/cards',ApiCardsViewSet,'cards')

urlpatterns = router.urls