from rest_framework import routers
from .views import RecycleViewSet

router = routers.SimpleRouter()
router.register("", RecycleViewSet)
urlpatterns = router.urls

