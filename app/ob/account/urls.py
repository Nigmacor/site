from django.urls import path
from django.urls import include
from django.contrib.auth.views import LoginView, LogoutView
from .views import register

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', register, name='register'),
]
