from django.shortcuts import render
from django.http import HttpResponse

def posts(request):
    return HttpResponse('<h1>Posts</h1>')

def load_post(request, slug):
    return HttpResponse(f'<h1>{slug} Nice!</h1>')