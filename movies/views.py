from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Movie

# Create your views here.
def handle_movie_home(request:HttpRequest):
    """ Function handles request for domain/movies"""
    movies =  Movie.objects.all().order_by("title")

    return render(request, "movies/index.html", {"movies": movies})

def handle_movie_by_id(request, movie_id):
    """ Function handles request for domain/movies"""
    if movie_id:
        return HttpResponse(content=f"<h1>You are Movie #{movie_id}'s page!</h1>")
    return HttpResponse(content=f"<h1>You are Temporary Movie page!</h1>")