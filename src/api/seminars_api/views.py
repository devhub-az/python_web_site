from django.shortcuts import get_object_or_404
#from rest_framework.decorators import api_view
from rest_framework.response import Response
from seminars.models import Seminar
from .serializers import (
    SeminarSerializer,
    SeminarCreateSerializer,
)
from rest_framework.pagination import PageNumberPagination
from django.core.paginator import Paginator
from rest_framework import viewsets
from .permissions import IsOrganizerOrReadOnly
from rest_framework import routers
from rest_framework.routers import DefaultRouter
# Create your views here.


class SeminarViews(viewsets.ModelViewSet):
    queryset = Seminar.objects.all()
    permission_classes = [IsOrganizerOrReadOnly]
    lookup_field = 'pk'

    def get_queryset(self):
        return Seminar.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SeminarSerializer
        else:
            return SeminarCreateSerializer

    def perform_create(self,serializer):
        serializer.save(organizer=self.request.user)

seminarRouter = routers.DefaultRouter()
seminarRouter.register(r'seminars', SeminarViews)