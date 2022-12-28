from django.shortcuts import render,get_object_or_404

# Create your views here.
from .post import posts

from .models import Post,Author,Tag


def starting_page(request):
    lates_posts=Post.objects.all().order_by('-date')[:3]
    return render(request,'blogApp/index.html',
                {
                    'posts':lates_posts,
                })


def post(request):
    sorted_posts=Post.objects.all().order_by('-date')
    return render(request,'blogApp/all_posts.html',
                {
                    'posts':sorted_posts,
                })
    


def post_detail(request,slug):
    identify_post=get_object_or_404(Post,slug=slug)
    return render(request,'blogApp/post_detail.html',
                {
                    "post":identify_post
                })
