from django.shortcuts import render, get_object_or_404

from .models import Post

def starting_page(request):
    latest_posts = Post.objects.all().order_by('-date')[:3]
    context = {
        'posts': latest_posts,
    }

    return render(request, 'blog/index.html', context)

def posts(request):
    all_posts = Post.objects.all().order_by('-date')
    context = {
        'posts': all_posts
    }

    return render(request, 'blog/posts.html', context)

def load_post(request, slug):
    identified_post = get_object_or_404(Post, slug=slug)
    context = {
        'post': identified_post,
    }

    return render(request, 'blog/full-post.html', context)