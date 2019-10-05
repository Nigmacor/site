from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('order/<id>', order_detail, name='order_detail_url'),
    path('tag', tag_list, name='tags_list_url'),
]
