from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def handle_movie_home(request:HttpRequest):
    """ Function handles request for domain/movies"""
    print(request)
    return HttpResponse(content="<h1>Movies's home</h1>")

def handle_movie_by_id(request, movie_id):
    """ Function handles request for domain/movies"""
    if movie_id:
        return HttpResponse(content=f"<h1>You are Movie #{movie_id}'s page!</h1>")
    return HttpResponse(content=f"<h1>You are Temporary Movie page!</h1>")