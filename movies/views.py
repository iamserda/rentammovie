from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Movie

# Create your views here.
def handle_movie_home(request:HttpRequest):
    """ Function handles request for domain/movies"""
    movies = Movie.objects.all().order_by("title")
    return render(request, "movies/movie.html", {"movies": movies})


def handle_movie_by_id(request: HttpRequest, movie_id):
    """ Function handles request for domain/movies"""
    movie = [movie for movie in Movie.objects.all() if movie.id == movie_id]
    if movie:
        return render(request, "movies/movie.html", {"movies": movie})
    return render(request, "movies/error.html", {"movies": movie})
