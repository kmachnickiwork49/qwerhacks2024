from django.urls import path

from . import views

app_name = "prompts"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:prompt_id>/", views.details, name="details"),
]
