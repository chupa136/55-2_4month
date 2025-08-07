from django.shortcuts import render, HttpResponse
from posts.models import Post

def home_view(request):
    return render(request, "home.html")

def first_view(request):
    return HttpResponse(f'hello world')

def html_view(request):
    return render(request,"base.html")

def post_list_view(request):
    posts = Post.objects.all()
    return render(request,"post_list.html", context={"posts": posts})