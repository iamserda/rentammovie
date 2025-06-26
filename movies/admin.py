from django.contrib import admin
from .models import Genre, Movie

# Register your models here.
admin.site.register([Movie, Genre])