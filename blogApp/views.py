from django.shortcuts import render

# Create your views here.

def starting_page(request):
    return render(request,'blogApp/index.html')


def post(request):
    return f'hallo world'


def post_detail(request):
    return f'word world'