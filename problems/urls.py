from django.urls import path
from .views import search_flipkart,index,search_microsoft,get_running_threads_count,search_google,search_amazon,search_must,auto

urlpatterns = [
    path('', index, name='home'),
    path('flipkart/', search_flipkart, name='Flipkart'),
    path('microsoft/', search_microsoft, name='Flipkart'),
    path('google/', search_google, name='Google'),
    path('amazon/', search_amazon, name='Amazon'),
    path('must-do/', search_must, name='mustDo'),
    path('auto/',auto,name="auto"),
    path('get_running_threads_count', get_running_threads_count, name='get_running_threads_count'),
    # Add other URLs as needed
]