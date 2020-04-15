from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'user'

urlpatterns = [
   path('register/',views.register,name='register'),
   path('login/',obtain_auth_token,name='login'),
]