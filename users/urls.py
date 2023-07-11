from rest_framework import routers
from django.urls import path, include
from .views import UserViewSet, ProfileView


router = routers.SimpleRouter()
router.register("", UserViewSet)


urlpatterns = [
    path("<int:pk>/profile", ProfileView.as_view()),
]
urlpatterns += router.urls
