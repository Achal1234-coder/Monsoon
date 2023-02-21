from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page

app_name = 'Account'

urlpatterns = [
    path('', cache_page(60*60)(Registration.as_view()), name=''),
    path('login', LogIn.as_view(), name='login'),
    path('home', login_required(Home.as_view()), name='home'),
    path('logout', LogOut.as_view(), name='logout')
]