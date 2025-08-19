from django.shortcuts import render, HttpResponse, redirect
from posts.models import Post
from posts.forms import PostForm
from django.contrib.auth.decorators import login_required

def home_view(request):
    return render(request, "home.html")

def first_view(request):
    return HttpResponse(f'hello world')

def html_view(request):
    return render(request,"base.html")

@login_required(login_url="login")
def post_list_view(request):
    posts = Post.objects.all()
    return render(request,"posts/post_list.html", context={"posts": posts})

@login_required(login_url="login")
def post_detail_view(request, post_id):
    post = Post.objects.get(id = post_id)
    return render(request, "posts/post_detail.html", context={"post": post})

@login_required(login_url="login")
def post_create_view(request):
    if request.method == "GET":
        form = PostForm()
        return render(request, "posts/post_create.html", context={"form": form})
    if request.method == "POST":
        form=PostForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, "posts/post_create.html", context={"form": form})
        else:
            title = form.cleaned_data.get("title")
            content = form.cleaned_data.get("content") 
            image = form.cleaned_data.get("image")
            Post.objects.create(title=title,content=content,image=image)
        return redirect("/posts")