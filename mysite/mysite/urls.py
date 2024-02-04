from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("home/", include("home.urls")),
    path("prompts/", include("prompts.urls")),
    path("apis/", include("apis.urls")),
    path("admin/", admin.site.urls),
]
