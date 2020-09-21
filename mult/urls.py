from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("mats", views.mats, name="mats"),
    path("<str:name>", views.greet, name="name")
]