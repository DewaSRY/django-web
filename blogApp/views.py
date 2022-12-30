from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import ListView,DetailView
from django.views import View
from django.urls import reverse
# Create your views here.
from .post import posts

from .models import Post,Author,Tag
from .form import CommentForm

class StaringPageView(ListView):
    template_name='blogApp/index.html'
    model=Post
    ordering=['-date']
    context_object_name='posts'


    def get_queryset(self):
        queryset=super().get_queryset()
        data=queryset[:3]
        return data

class AllPostView(ListView):
    template_name='blogApp/all_posts.html'
    model=Post
    ordering=['-date']
    context_object_name='posts'


class SingelPostView(View):
    def is_save_post(self,request,post_id):
        stored_posts=request.session.get('stored_posts')
        if stored_posts is not None:
            is_save_for_later=post_id in stored_posts
        else:
            is_save_for_later=False
        return is_save_for_later
    
    def get(self,request,slug):
        post=Post.objects.get(slug=slug)
       
        context={
            'post':post,
            'post_tags':post.tags.all(),
            'Comment_Form':CommentForm(),
            'Comment':post.comment.all().order_by('-id'),
            'is_save_for_later':self.is_save_post(request,post.id)
            
        }
        return render(request,'blogApp/post_detail.html',context)
    
    def post(self,request,slug):
        Comment_Form=CommentForm(request.POST)
        post=Post.objects.get(slug=slug)
        
        if Comment_Form.is_valid():
            comment=Comment_Form.save(commit=False)
            comment.post=post
            comment.save()
            return HttpResponseRedirect(reverse("post_detail_pages",args=[slug]))
        
        post=Post.object.get(slug=slug)
        context={
            'post':post,
            'post_tags':post.tags.all(),
            'Comment_Form':CommentForm(),
            'Comment':post.comment.all().order_by('-id'),
            'is_save_for_later':self.is_save_post(request,post_id)
            

            
        }
        return render(request,'blogApp/post_detail.html',context)



class ReadLaterView(View):
    def get(self,request):
        stored_posts=request.session.get('stored_posts')
        context={}
        
        if stored_posts is None or len(stored_posts)==0:
            context['posts']=[]
            context['has_posts']=False
        else:
            posts=Post.objects.filter(id__in=stored_posts)
            context['posts']=posts
            context['has_posts']=True
            
        return render(request,'blogApp/stored_post.html',context)
    
    def post(self,request):
        stored_posts=request.session.get('stored_posts')
        if stored_posts is None:
            stored_posts=[]
            
        post_id=int(request.POST['post_id'])
        
        if post_id not  in stored_posts:
            stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)
            
        request.session['stored_posts']=stored_posts
        
        return HttpResponseRedirect('/')