import datetime

from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


class Blog(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, primary_key=True)
    subscribers = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user}'s blog: {self.subscribers} subscribers"

    objects = models.Manager()


class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    published = models.DateTimeField(default=datetime.datetime.now())

    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} published at {self.published}"

    objects = models.Manager()


class ReadPost(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} read a {self.post} post"

    objects = models.Manager()
