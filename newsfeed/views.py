from django.shortcuts import render

from .models import Subscriber
from blog.models import Blog, Post

# Create your views here.


def newsfeedPage(request):

    context = {}
    recommendations = []
    posts = []
    subscriptions = Subscriber.objects.filter(user=request.user)
    for s in subscriptions:
        recommendations = Blog.objects.exclude(user=request.user).exclude(user=s.blog.user)
        posts = Post.objects.filter(blog__user=s.blog.user)

    if recommendations and subscriptions:
        context = {
            'subscriptions': subscriptions,
            'recommendations': recommendations,
            'posts': posts
        }

    return render(request=request, template_name='blogs/index.html', context=context)
