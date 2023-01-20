from django.urls import path
from .views import MapViewSet, MapUpdate
from rest_framework import routers

app_name = "maps"

router = routers.SimpleRouter()
router.register("", MapViewSet)

urlpatterns = [
    path("update", MapUpdate.as_view()),
]

urlpatterns += router.urls
