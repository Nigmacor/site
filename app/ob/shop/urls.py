from django.urls import path
from .views import *

urlpatterns = [
    path('', shop, name='shop'),
]