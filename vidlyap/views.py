from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# req = HttpRequest("movies/")
# Create your views here.
def handle_home(request:HttpRequest):
    print(request)
    return HttpResponse(content="<h1>You are home</h1>")