from django.urls import path
from . import views

app_name = "encyclopedia"

urlpatterns = [ 
    path("", views.index, name="index"),
    path("search_entry", views.search_entry, name="search_entry"),
    path("<str:title>", views.get_entry, name="get_entry"),
]