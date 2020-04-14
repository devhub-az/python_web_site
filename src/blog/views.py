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

