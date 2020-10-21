from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.newsfeedPage, name='newsfeed'),
    path('subscribe/<int:blog_id>', views.subscribe, name='subscribe'),
    path('unsubscribe/<int:blog_id>/<int:subscription_id>', views.unsubscribe, name='unsubscribe'),
    path('read_post/<int:post_id>', views.read_post, name='read_post'),
]
