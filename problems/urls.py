from django.urls import path
from .views import search_solution

urlpatterns = [
    path('', search_solution, name='search_solution'),
    # Add other URLs as needed
]