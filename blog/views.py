from datetime import date

from django.shortcuts import render
from django.http import HttpResponse

from .models import Post

all_posts = Post.objects.all()

# Helper functions
def get_date(post):
    return post['date']

def starting_page(request):
    latest_posts = Post.objects.order_by('-date')
    context = {
        'posts': latest_posts,
    }

    return render(request, 'blog/index.html', context)

def posts(request):
    context = {
        'posts': all_posts
    }

    return render(request, 'blog/posts.html', context)

def load_post(request, slug):
    identified_post = next(post for post in all_posts if post.slug == slug)
    context = {
        'post': identified_post,
    }

    return render(request, 'blog/full-post.html', context)