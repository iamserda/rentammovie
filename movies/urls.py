from django.urls import path
from . import views



urlpatterns = [
    path("", views.handle_movie_home, name="handle_home"),
    path("<int:movie_id>/", views.handle_movie_by_id, name="handle_a_movie")
    ]