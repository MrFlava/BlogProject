from django.db import models
from django.contrib.auth import get_user_model

from blog.models import Blog

# Create your models here.


class Subscriber(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("user", "blog")

    def __str__(self):
        return f"{self.user} subscribed to {self.blog} blog"

    objects = models.Manager()
