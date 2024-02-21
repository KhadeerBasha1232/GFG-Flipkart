from django.urls import path
from .views import search_flipkart,index,search_microsoft,search_google,search_amazon,search_must,auto

urlpatterns = [
    path('', index, name='home'),
    path('flipkart/', search_flipkart, name='Flipkart'),
    path('microsoft/', search_microsoft, name='Flipkart'),
    path('google/', search_google, name='Google'),
    path('amazon/', search_amazon, name='Amazon'),
    path('must-do/', search_must, name='mustDo'),
    path('auto/',auto,name="auto"),
    # Add other URLs as needed
]