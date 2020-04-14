from django.urls import path,include
from . import views
from .posts_api import views as post_views
from .seminars_api import views as seminar_views
from .comments_api import views as comment_views
from .comments_api.views import *

app_name = 'api'




urlpatterns = [
    #path('posts/',views.api_post_list,name='api-post-list'),
    #path('post/<int:post_id>/',views.api_post_detail,name='api-post-detail'),
    path('',include(post_views.blogapiRouter.urls)),
    path('',include(seminar_views.seminarRouter.urls)),
    # path('comment/<pk>/',CommentDetailAPIView.as_view()),
    # path('comment/',CommentListAPIView.as_view()),
    path('',include(comment_views.commentapiRouter.urls)),
]


