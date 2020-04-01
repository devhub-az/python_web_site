from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.pagination import PageNumberPagination

# Create your views here.

class CustomPagination(PageNumberPagination):
    page_size = 10
    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'per_page': self.page_size,
            'first_page': 1,
            'last_page': self.page.paginator.num_pages,
            'next': self.get_next_link(),
            'current_page': int(self.request.GET.get('page',1)),
            'previous': self.get_previous_link(),
            'from': 1,
            'to': 1,
            'results': data
        })


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
