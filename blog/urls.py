from django.urls import path
from . import views

app_name = 'post'


urlpatterns = [
    path('',views.post_list,name='post-list'),
    path('create/',views.post_create,name='post-create'),
    path('<str:post_slug>/',views.post_detail,name='post-detail'),
    path('<str:post_slug>/edit/',views.post_edit,name='post-edit'),
    path('<str:post_slug>/delete/',views.post_delete,name='post-delete'),
]