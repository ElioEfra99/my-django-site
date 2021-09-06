from django.db import models
from django.db.models.fields.related import ForeignKey
from django.utils.translation import override

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    emai_address = models.EmailField(max_length=254)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

class Tag(models.Model):
    caption = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f'{self.caption}'

class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=249)
    image_name = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    slug = models.SlugField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return f'{self.title}'
    
    
