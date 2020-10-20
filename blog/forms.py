from .models import Post, Blog
from django.forms import ModelForm


class PostForm(ModelForm):
    class Meta:

        model = Post
        fields = ['title', 'content']

