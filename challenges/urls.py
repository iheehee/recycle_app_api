from rest_framework import routers
from .views import ChallengeViewSet

router = routers.DefaultRouter()
router.register("", ChallengeViewSet)
urlpatterns = router.urls
