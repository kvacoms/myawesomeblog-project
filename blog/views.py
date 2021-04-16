from django.shortcuts import render, get_object_or_404

# Create your views here.
from blog.models import Post


def showblog(request):
    posts = Post.objects
    return render(request, 'blog.html', {'posts': posts})


def specific_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'specific_post.html', {'post': post})
