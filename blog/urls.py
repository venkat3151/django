from django.urls import path
from . import views

urlpatterns = [
    path('', views.new_post, name ='blog'),
    path('about/', views.about, name ='blog-about'),
]