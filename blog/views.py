from django.shortcuts import render
from django.http import HttpResponse

def starting_page(request):
    return render(request, 'blog/index.html')

def posts(request):
    return render(request, 'blog/posts.html')

def load_post(request, slug):
    context = {
        'post_name': slug
    }

    return render(request, 'blog/full-post.html', context)