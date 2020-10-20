from django.contrib import admin
from blog.models import Blog, Post

# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    model = Blog


class PostAdmin(admin.ModelAdmin):
    model = Post


admin.site.register(Blog, BlogAdmin)
admin.site.register(Post, PostAdmin)
