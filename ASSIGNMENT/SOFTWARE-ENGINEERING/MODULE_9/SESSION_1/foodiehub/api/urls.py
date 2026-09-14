from django.urls import path
from .views import hello_spotify

urlpatterns = [
    path('api/hello_spotify/',hello_spotify)
]