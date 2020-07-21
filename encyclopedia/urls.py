from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("create", views.create, name="create"),
    path("edit/<str:title>", views.edit, name="edit"),
    path("wiki/", views.randomPagergen, name="random"),
    path("about/", views.about, name="about"),
    path("rules/", views.rules, name="rules")
]
