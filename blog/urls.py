from django.urls import path

from . import views

urlpatterns = [
    path('', views.myblogPage, name='my_blog'),
    path('create_post', views.createpostPage, name='create_post'),
]
