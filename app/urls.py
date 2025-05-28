from django.urls import path
from .views import home,blog_view,life_style,page_404,gallery,sport,author,gallery_single,blog_single,contact

urlpatterns = [
    path('',home,name="home"),
    path('blog-view/',blog_view,name="blog-view"),
    path('life_style/',life_style,name="life_style"),
    path('gallery/',gallery,name="gallery"),
    path('page_404/',page_404,name="page_404"),
    path('author/',author,name="author"),
    path('sport/',sport,name="sport"),
    path('contact/',contact,name="contact"),
    path('gallery_single/',gallery_single,name="gallery_single"),
    path('blog_single/<int:id>/',blog_single,name="blog_single"),
]