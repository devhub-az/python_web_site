from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.index, name='main-page'),
    path('create/', views.create, name='post-create'),
    path('<str:slug>/', views.show, name='post-detail'),
    path('<str:slug>/edit/', views.edit, name='post-edit'),
    path('<str:slug>/delete/', views.delete, name='post-delete'),
    path('like/', views.like, name='post-like'),
]
