from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('client/', client, name='client'),
    path('search/', search, name='search'),
    path('thanks/', thanks, name='thanks')
]
