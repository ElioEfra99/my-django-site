from django.contrib import admin
from .models import Post, Tag, Author

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
