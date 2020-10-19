from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


class Blog(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f"{self.user}'s blog"

    objects = models.Manager()
