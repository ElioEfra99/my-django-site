from django.urls import path

from blog import views

urlpatterns = [
    path('', views.posts),
    path('<slug:slug>', views.load_post), # The <"slug":slug> segment is called a path converter
]
