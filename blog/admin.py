from django.contrib import admin
from .models import Post, Tag, Author

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('author', 'date', 'tags')
    list_display = ('title', 'date', 'author')
    date_hierarchy = 'date'


admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
