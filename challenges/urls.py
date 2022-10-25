from rest_framework import routers
from .views import ChallengeViewSet

router = routers.SimpleRouter()
router.register("", ChallengeViewSet)
urlpatterns = router.urls
