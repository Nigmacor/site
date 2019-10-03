from django.urls import path

from .views import *

urlpatterns = [
    path('registration/', registration, name='registration'),
    path('regjur/', regjur, name='regjur'),
    path('regphis/', regphis, name='regphis'),
    path('autorisation/', autorisation, name='autorisation'),
]