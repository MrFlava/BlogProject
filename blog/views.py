from django.shortcuts import render, redirect

from blog.models import Blog
from blog.forms import PostForm
from .models import Post
# Create your views here.


def myblogPage(request):
    blog = Blog.objects.get(pk=request.user)
    return render(request=request, template_name="my_blog/index.html", context={'blog': blog})


def createpostPage(request):
    error = ''

    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            blog = Blog.objects.get(pk=request.user)
            post = Post()
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post.blog = blog
            post.save()

            return redirect('/blog')

        else:
            error = 'Some error'

    form = PostForm()

    data = {
        'form': form,
        'error': error

    }

    return render(request=request, template_name='my_blog/create_post.html', context=data)


