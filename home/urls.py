from django.urls import path

from . import views

urlpatterns = [
    path('', views.homePage, name='homepage'),
    path('sign-in/', views.signinPage, name='sign-in'),
]
