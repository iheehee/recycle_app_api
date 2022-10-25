from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("recycles/", include("recycles.urls")),
    path("users/", include("users.urls")),
    path("challenges/",include("challenges.urls"))
]
