from django.urls import path

from blog import views

urlpatterns = [
    path('', views.starting_page, name='starting-page'),
    path('posts/', views.posts, name='posts-page'),
    path('posts/<slug:slug>', views.load_post, name='full-post-page'), # The <"slug":slug> segment is called a path converter
]
