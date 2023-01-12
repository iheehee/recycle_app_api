from django.urls import path
from . import views

app_name = "maps"

urlpatterns = [
    path("update", views.MapUpdate.as_view()),
]
