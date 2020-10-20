from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

from blog.models import Blog, Post
# Create your views here.


def homePage(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }

    return render(request, 'homepage/index.html', context)


def signinPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            blog = Blog.objects.get(pk=user)
            if not blog:
                new_blog = Blog(user=user)
                new_blog.save()
            return redirect('/')

    return render(request=request, template_name='sign-in/index.html')
