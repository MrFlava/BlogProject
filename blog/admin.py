from django.contrib import admin
from blog.models import Blog, Post, ReadPost

# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    model = Blog


class PostAdmin(admin.ModelAdmin):
    model = Post


class ReadPostAdmin(admin.ModelAdmin):
    model = ReadPost


admin.site.register(Blog, BlogAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(ReadPost, ReadPostAdmin)
