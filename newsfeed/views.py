from django.shortcuts import render, get_object_or_404, redirect

from .models import Subscriber
from blog.models import Blog, Post, ReadPost

# Create your views here.


def newsfeedPage(request):

    recommendations = []
    posts = []
    user_and_subscriptions = [request.user]
    subscriptions = Subscriber.objects.filter(user=request.user)
    for s in subscriptions:
        user_and_subscriptions.append(s.blog.user)
        posts += Post.objects.filter(blog=s.blog)
    if len(user_and_subscriptions) == 1:
        recommendations = Blog.objects.exclude(user__in=user_and_subscriptions)
    else:
        recommendations += Blog.objects.exclude(user__in=user_and_subscriptions)

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

        return redirect('newsfeed')


def unsubscribe(request, blog_id, subscription_id):

    if request.method == "GET":
        blog = get_object_or_404(Blog, pk=blog_id)
        blog.subscribers -= 1

        delete_subscription = Subscriber.objects.get(pk=subscription_id)

        delete_subscription.delete()

        blog.save()

        return redirect('newsfeed')


def read_post(request, post_id):

    if request.method == "POST":
        post = get_object_or_404(Post, pk=post_id)
        read_new_post = ReadPost(user=request.user, post=post)
        read_new_post.save()

        context = {
            "post": post,
            "is_read": True
        }

        return render(request=request, template_name='blogs/index.html', context=context)
