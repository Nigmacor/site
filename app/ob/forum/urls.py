from django.urls import path
from .views import *

urlpatterns = [
    path('', forum, name='forum_url'),
	path('forum/<id>', forum_detail, name='forum_detail_url'),
    path('them/', forum_list, name='forum_list_url'),
]