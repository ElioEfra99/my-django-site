from django.db import models
from django.core.validators import MinLengthValidator


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    emai_address = models.EmailField()

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
    date = models.DateField(auto_now=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, related_name='posts', null=True)
    tags = models.ManyToManyField(Tag)
    
    def __str__(self) -> str:
        return self.title
