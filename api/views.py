from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.pagination import PageNumberPagination
from django.core.paginator import Paginator

# Create your views here.

class CustomPagination(PageNumberPagination):
    page_size = 10
    def get_paginated_response(self, data):
        posts = Post.objects.all()
        current_page = int(self.request.GET.get('page',1))
        paginator = Paginator(posts,self.page_size)
        from_ = paginator.page(current_page).start_index()
        to_ = paginator.page(current_page).end_index()
        return Response({
            'count': self.page.paginator.count,
            'per_page': self.page_size,
            'first_page': 1,
            'last_page': self.page.paginator.num_pages,
            'next': self.get_next_link(),
            'current_page': current_page,
            'previous': self.get_previous_link(),
            'from': from_,
            'to': to_,
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
