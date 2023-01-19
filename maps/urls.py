from django.urls import path
from .views import MapViewSet, MapUpdate
from rest_framework import routers

app_name = "maps"

router = routers.SimpleRouter()
router.register("", MapViewSet)

# urlpatterns = [
#    path("update", MapUpdate.as_view()),
#    path("", MapViewSet.as_view()),
# path("search", MapViewSet.search.as_view()),
# ]

# urlpatterns += router.urls
urlpatterns = router.urls
