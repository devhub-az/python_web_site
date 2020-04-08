from django.urls import path
from . import views

app_name = 'seminar'

urlpatterns = [
    path('',views.seminar_list,name='seminar-list'),
    path('create/',views.seminar_create,name='seminar-create'),
    path('<int:pk>/', views.seminar_detail, name='seminar-detail'),
    path('<int:pk>/edit',views.seminar_edit,name='seminar-edit'),
]