from django.urls import path
from . import views

# app_name = "encyclopedia"

urlpatterns = [ 
    path("", views.index, name="index"),
    path("wiki/search_entry", views.search_entry, name="search_entry"),
    path("wiki/create_entry", views.create_entry, name="create_entry"),
    path("wiki/edit/<str:title>", views.edit_entry, name="edit_entry"),
    path("wiki/random", views.random_entry, name="random_entry"),
    path("wiki/<str:title>", views.get_entry, name="get_entry"),
]