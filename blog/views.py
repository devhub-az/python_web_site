from django.shortcuts import render,get_object_or_404,redirect,reverse,HttpResponseRedirect
from .models import Post
from .forms import PostForm
from django.http import JsonResponse
# Create your views here.



def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts,
    }
    return render(request,'post/post_list.html',context)

def post_create(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST or None)
        if form.is_valid():
            postForm = form.save(commit = False)
            postForm.author = request.user
            postForm.save()
            return HttpResponseRedirect(reverse('post:post-detail', kwargs={'post_slug': postForm.slug}))
    context = {
        'form':form,
    }
    return render(request,'post/post_create.html',context)


def post_detail(request,post_slug):
    post = get_object_or_404(Post,slug=post_slug)
    context = {
        'post':post
    }
    return render(request,'post/post_detail.html',context)

def post_edit(request,post_slug):
    post = get_object_or_404(Post,slug=post_slug)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST or None, instance=post)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.update = True
            new_form.save()
            return HttpResponseRedirect(reverse('post:post-detail', kwargs={'post_slug': new_form.slug}))
    context = {'form': form}
    return render(request, 'post/post_edit.html', context)

def post_delete(request,post_slug):
    post = get_object_or_404(Post,slug = post_slug)
    post.deleted = True
    post.save()
    return redirect('post:post-list')

def post_like(request):
    id_ = request.GET.get('id')   #comes from fron with ajax
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
        'unlikes_count': unlikes_count,
    }
    return JsonResponse(data)