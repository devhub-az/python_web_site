# from rest_framework.decorators import api_view
from django.core.paginator import Paginator
from rest_framework import routers
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import permissions
from blog.models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import (
    PostSerializer,
    PostCreateSerializer,
)
from rest_framework import filters
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.

class CustomPagination(PageNumberPagination):
    page_size = 10

    def get_paginated_response(self, data):
        posts = Post.objects.filter(deleted=False)
        current_page = int(self.request.GET.get('page', 1))
        paginator = Paginator(posts, self.page_size)
        from_ = paginator.page(current_page).start_index()
        to_ = paginator.page(current_page).end_index()
        return Response({
            'meta': {
                'count': self.page.paginator.count,
                'per_page': self.page_size,
                'first_page': 1,
                'last_page': self.page.paginator.num_pages,
                'next': self.get_next_link(),
                'current_page': current_page,
                'previous': self.get_previous_link(),
                'from': from_,
                'to': to_,
            },
            'data': data
        })


"""
@api_view(['GET'])
def api_post_list(request):
    paginator = CustomPagination()
    posts = Post.objects.all()
    result_page = paginator.paginate_queryset(posts, request)
    serializer = PostSerializer(result_page,many=True)
    return paginator.get_paginated_response(serializer.data)

@api_view(['GET'])
def api_post_detail(request,post_id):
    post = get_object_or_404(Post,id=post_id)
    serializer = PostSerializer(post,many=False)
    return Response(serializer.data)
"""


class PostViews(viewsets.ModelViewSet):
    queryset = Post.objects.filter(deleted=False)
    permission_classes = [IsAuthorOrReadOnly]
    pagination_class = CustomPagination
    lookup_field = 'pk'
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    def get_queryset(self):
        return Post.objects.filter(deleted=False)

    def get_object(self):
        obj = super().get_object()
        obj.viewed += 1
        obj.save()
        return obj

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PostSerializer
        else:
            return PostCreateSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_destroy(self, instance):
        post = instance
        post.deleted = True
        post.save()

    def perform_update(self, serializer):
        serializer.save(updated=True)

    @action(detail=True,methods=['get'],permission_classes=[permissions.IsAuthenticated])
    def likes(self,request,pk=None):
        obj = self.get_object()
        current_user = request.user
        liked = False
        likes_count = obj.total_likes()
        dislikes_count = obj.total_dislikes()
        if current_user in obj.likes.all():
            liked = False
            obj.likes.remove(current_user)
            likes_count -= 1
        else:
            liked = True
            if current_user in obj.dislikes.all():
                obj.dislikes.remove(current_user)
                dislikes_count -= 1
                obj.likes.add(current_user)
                likes_count += 1
            else:
                obj.likes.add(current_user)
                likes_count += 1
        data = {
            "liked": liked,
            "id_": obj.id,
            'likes_count': likes_count,
            'dislikes_count': dislikes_count,
        }
        return Response(data)

    @action(detail=True, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def dislikes(self, request, pk=None):
        obj = self.get_object()
        current_user = request.user
        disliked = False
        likes_count = obj.total_likes()
        dislikes_count = obj.total_dislikes()
        if current_user in obj.dislikes.all():
            disliked = False
            obj.dislikes.remove(current_user)
            dislikes_count -= 1
        else:
            disliked = True
            if current_user in obj.likes.all():
                obj.likes.remove(current_user)
                likes_count -= 1
                obj.dislikes.add(current_user)
                dislikes_count += 1
            else:
                obj.dislikes.add(current_user)
                dislikes_count += 1
        data = {
            "disliked": disliked,
            "id_": obj.id,
            'likes_count': likes_count,
            'dislikes_count': dislikes_count,
        }
        return Response(data)



blogapiRouter = routers.DefaultRouter()
blogapiRouter.register(r'posts', PostViews)
