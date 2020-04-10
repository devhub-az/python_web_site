from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponseRedirect
from .models import Post
from .forms import PostForm
from django.http import JsonResponse
from django.core.paginator import Paginator

# Create your views here.


def index(request):
    return render(request, 'post/sections/index.html',{})


def create(request):
    return render(request, 'post/sections/post_create.html', {})


def show(request, post_pk):
    return render(request, 'post/sections/show.html',{})


def edit(request, post_pk):
    return render(request, 'post/sections/edit.html',{})


def delete(request, post_pk):
    return redirect('post:main-page')


def like(request):
    id_ = request.GET.get('id')  # comes from front with ajax
    post = get_object_or_404(Post, id=id_)
    user = request.user
    liked = False
    likes_count = post.total_likes()
    if user in post.likes.all():
        liked = False
        post.likes.remove(user)
        likes_count -= 1
    else:
        liked = True
        post.likes.add(user)
        likes_count += 1
    # data send to front with ajax
    data = {
        "liked": liked,
        "id_": post.id,
        'likes_count': likes_count,
    }
    return JsonResponse(data)
