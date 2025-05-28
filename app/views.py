from django.shortcuts import render,redirect
from .models import Blog,Category,Comment
from utils.views import group_queryset
from django.core.paginator import Paginator
from .forms import CommentForm
from django.contrib import messages

# Create your views here.

def blog_single(request,id):
    
    if request.method == "POST":
        form = CommentForm(request.POST)

        if not request.user.is_authenticated:
            return redirect('login ')

        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
        
        else:
            messages.add_message(request,level=messages.ERROR,message="malumotlar notogri")
    coms = Comment.objects.filter(blog = id)
    sports = Blog.objects.filter(category__name = "Sports")
    business = Blog.objects.filter(category__name="Business")
    technology = Blog.objects.filter(category__name = "Gadgets and Technology")
    blog = Blog.objects.get(id = id)
    related_blogs = Blog.objects.filter(category = blog.category)
    context = {
        'comment' : coms,    
        'sports' : sports,
        'sp0' : blog,
        "business" : business,
        'technology' : technology,
        'related_blogs' : related_blogs,
    }

    return render(request,'blog_single.html',context)

def contact(request):
    return render(request,'contact.html')

def gallery_single(request):
    sports = Blog.objects.filter(category__name = "Sports").first()
    business = Blog.objects.filter(category__name="Business")
    context = {
        'sp8' : sports,
        "business" : business,
    }
    return render(request,'gallery_single.html',context)

def life_style(request):
    technology = Blog.objects.filter(category__name = "Gadgets and Technology")
    sports = Blog.objects.filter(category__name = "Sports")
    business = Blog.objects.filter(category__name="Business")
    blogs = Blog.objects.order_by("-id")[:8]
    context = {
        "business" : business,
        'technology' : technology,
        'sports' : sports,
        'blogs' : blogs,
    }
    return render(request,"life_style.html",context)
def page_404(request):
    technology = Blog.objects.filter(category__name = "Gadgets and Technology")
    sports = Blog.objects.filter(category__name = "Sports")
    business = Blog.objects.filter(category__name="Business")
    context = {
        "business" : business,
        'technology' : technology,
        'sports' : sports,
    }
    return render(request,"404.html",context)
def gallery(request):
    technology = Blog.objects.filter(category__name = "Gadgets and Technology")
    sports = Blog.objects.filter(category__name = "Sports")
    business = Blog.objects.filter(category__name="Business")
    context = {
        "business" : business,
        'technology' : technology,
        'sports' : sports,
    }
    return render(request,"gallery.html",context)
def sport(request):
    technology = Blog.objects.filter(category__name = "Gadgets and Technology")
    sports = Blog.objects.filter(category__name = "Sports")
    business = Blog.objects.filter(category__name="Business")
    context = {
        "business" : business,
        'technology' : technology,
        'sports' : sports,
    }
    return render(request,"sport.html",context)
def author(request):
    business = Blog.objects.filter(category__name="Business")
    technology = Blog.objects.filter(category__name = "Gadgets and Technology")
    sports = Blog.objects.filter(category__name = "Sports")
    context = {
        'business' : business,
        'technology' : technology,
        'sports' : sports,
    }
    return render(request,"author.html",context)

def home(request):
    header = Blog.objects.order_by("-id")[:3]
    recent_new = Category.custom.filter(translations__name__in = ["Politics","Technology"])
    blogs = Blog.objects.all()
    # business = Blog.objects.filter(category__name="Business")
    business = Category.custom.get_category("Business")
    sports = Blog.objects.filter(category__translations__name = "Sports")
    # technology = Blog.objects.filter(category__name = "Gadgets and Technology")
    technology = Blog.objects.filter(category__translations__name = "Technology")
    # gatget_blogs = Blog.objects.filter(category = technology)
    # gatgets_paginator = Paginator(gatget_blogs,5)
    # page_number = request.GET.get("page",1) 
    # gatgets_by_page = gatgets_paginator.get_page(page_number)


    life_style = Blog.objects.filter(category__translations__name = "Life style")
    travel = Blog.objects.filter(category__translations__name = "Travels")
    weather = Blog.objects.filter(category__translations__name = "Weather")
    last_blog = Blog.objects.last()
    categories = Category.objects.all()
    recent_posts = Blog.objects.filter()
    reviews = ()
    # def group_queryset(n,queryset):
    #     result = []
    #     temp = []
    #     for q in queryset:
    #         temp.append(q)
    #         if len(temp) == n:
    #             result.append(temp)
    #             temp = []
    #     return result

    context = {
        # 'gatgets_by_page' : gatgets_by_page,
        'banner' : header,
        'recent_new' : recent_new,
        'blogs' : group_queryset(2,blogs),
        "business" : business,
        "sports" : sports,
        "technology" : technology,
        "life_style" : life_style,
        "travel" : travel,
        "weather" : weather,
        "last_blog" : last_blog,
        "categories" : categories,
    }

    return render(request,"index.html",context)

def blog_view(request):
    technology = Blog.objects.filter(category__name = "Gadgets and Technology")
    sports = Blog.objects.filter(category__name = "Sports").first()
    business = Blog.objects.filter(category__name="Business")
    context = {
        "business" : business,
        'technology' : technology,
        'sp0' : sports,
    }
    return render(request,'blog.html',context)