from django.shortcuts import render

# Create your views here.
from .post import posts



def starting_page(request):
    sorted_posts=sorted(posts,key=lambda post:post['date'])
    lates_posts=sorted_posts[-3:]
    return render(request,'blogApp/index.html',
                {
                    'posts':lates_posts,
                })


def post(request):
    sorted_posts=sorted(posts,key=lambda post:post['date'])
    return render(request,'blogApp/all_posts.html',
                {
                    'posts':sorted_posts,
                })
    


def post_detail(request,slug):
    identify_post=next(post for post in posts if post['slug']==slug )
    return render(request,'blogApp/post_detail.html',
                {
                    "post":identify_post
                })
