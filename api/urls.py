from django.urls import path
from . import views


app_name = 'api'
urlpatterns = [
    path('posts/',views.api_post_list,name='api-post-list'),
    path('post/<int:post_id>/',views.api_post_detail,name='api-post-detail'),
]