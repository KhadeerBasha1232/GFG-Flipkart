from django.urls import path
from .views import search_flipkart,index,search_microsoft,search_google,search_amazon

urlpatterns = [
    path('', index, name='home'),
    path('flipkart/', search_flipkart, name='Flipkart'),
    path('microsoft/', search_microsoft, name='Flipkart'),
    path('google/', search_google, name='Google'),
    path('amazon/', search_amazon, name='Amazon'),
    # Add other URLs as needed
]