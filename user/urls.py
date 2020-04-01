
from django.urls import path
from . import views

app_name = 'user'


urlpatterns = [
    path('register/',views.user_register,name='register'),
    path('login/',views.user_login,name='login'),
    path('settings/', views.user_settings,name='settings'),
    path('logout/', views.user_logout, name='logout'),
    path('passwordchange/',views.user_password_change,name='passwordchange'),
]
