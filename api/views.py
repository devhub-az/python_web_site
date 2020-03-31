from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from blog.models import Post
from .serializers import PostSerializer
# Create your views here.



@api_view(['GET'])
def api_post_list(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def api_post_detail(request,post_id):
    post = get_object_or_404(Post,id=post_id)
    serializer = PostSerializer(post,many=False)
    return Response(serializer.data)
