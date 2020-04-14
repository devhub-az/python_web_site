from comments.models import Comment
from rest_framework import generics,status
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import (
    CommentSerializer,
    CommentCreateSerializer
    )
from .permissions import IsUserOrReadOnly
from rest_framework.routers import DefaultRouter
from django.utils import timezone
from rest_framework.views import exception_handler

router = DefaultRouter()

 
class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    permission_classes = [IsUserOrReadOnly]
    lookup_field =  'pk'


    def get_queryset(self):
        return Comment.objects.filter()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CommentSerializer
        else:
            return CommentCreateSerializer

   
    def perform_destroy(self,instance):
        comment = instance
        comment.active = False
        comment.save()

    def perform_update(self, serializer):
        serializer.save(updated=True,updated_at=timezone.now())
    
    def update(self, request, *args, **kwargs):
        super(CommentView, self).update(request, args, kwargs)
        response = {
                    "status_code": status.HTTP_200_OK,
                    "message": "Successfully updated",
                  }
        return Response(response)
        

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        super(CommentView, self).create(request, args, kwargs)       
        response = {
                    "status_code": status.HTTP_200_OK,
                    "message": "Successfully created",
                  }
     
        return Response(response)

commentapiRouter = DefaultRouter()
commentapiRouter.register(r'comment', CommentView)