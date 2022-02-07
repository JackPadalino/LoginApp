from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import profileView,registerView

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='main/home.html'),name='logout'),
    path('profile/',profileView,name='profile'),
    path('register/',registerView,name='register'),
]