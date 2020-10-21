from django.shortcuts import render, get_object_or_404

from .models import Subscriber
from blog.models import Blog, Post

# Create your views here.


def newsfeedPage(request):

    recommendations = []
    posts = []
    user_and_subscriptions = [request.user]
    subscriptions = Subscriber.objects.filter(user=request.user)
    for s in subscriptions:
        user_and_subscriptions.append(s.blog.user)
        recommendations = Blog.objects.exclude(user__in=user_and_subscriptions)
        posts += Post.objects.filter(blog=s.blog)

    context = {
            'subscriptions': subscriptions,
            'recommendations': recommendations,
            'posts': posts
        }

    return render(request=request, template_name='blogs/index.html', context=context)


def subscribe(request, blog_id):

    if request.method == "POST":
        blog = get_object_or_404(Blog, pk=blog_id)
        blog.subscribers += 1

        blog.save()

        new_subscriber = Subscriber(user=request.user, blog=blog)

        new_subscriber.save()

        return render(request, 'blogs/index.html')


def unsubscribe(request, blog_id, subscription_id):

    if request.method == "GET":
        blog = get_object_or_404(Blog, pk=blog_id)
        blog.subscribers -= 1

        blog.save()

        delete_subscription = Subscriber.objects.get(pk=subscription_id)

        delete_subscription.delete()

        return render(request, 'blogs/index.html')
