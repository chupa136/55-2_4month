from django.shortcuts import render, HttpResponse

# Create your views here.

def first_view(request):
    return HttpResponse(f'hello world')

def html_view(request):
    return render(request,"base.html")