from django.urls import path
from . import views



urlpatterns = [
    path("", views.handle_home, name="handle_home"),
    path("1/", views.handle_fwd1, name="handle_")
    ]