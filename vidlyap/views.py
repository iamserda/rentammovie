from django.shortcuts import render
from django.http import HttpResponse

# req = HttpRequest("movies/")
# Create your views here.
def index(request):
    return HttpResponse("<h1>You are home</h1>")