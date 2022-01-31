from turtle import home
from django.urls import path
from .views import homePageView

urlpatterns = [
    path('', homePageView, name='home'),
    path('home/', homePageView, name='home'),
]
