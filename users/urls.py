from rest_framework import routers
from .views import UserViewSet, ProfileView


router = routers.SimpleRouter()
router.register("users", UserViewSet)
router.register("profile", ProfileView)
urlpatterns = router.urls
