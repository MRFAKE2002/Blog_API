from django.contrib import admin

from .models import Post

@admin.register(Post)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'status']
    