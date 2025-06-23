from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def handle_home(request:HttpRequest):
    """ Function handles request for domain/movies"""
    print(request)
    return HttpResponse(content="<h1>You are in Movies App's home</h1>")

def handle_fwd1(request:HttpRequest):
    """ Function handles request for domain/movies"""
    return HttpResponse(content="<h1>You are #1</h1>")