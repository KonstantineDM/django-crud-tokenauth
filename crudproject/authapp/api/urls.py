from authapp.api import views
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'authapp'
urlpatterns = [
    path('register', views.register, name='register'),
    path('login', obtain_auth_token, name='login'),
]
