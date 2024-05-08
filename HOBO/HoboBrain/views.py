from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request, "homepage.html")

def profile(request):
    return render(request, "profile.html")

def content(request):
    return render(request, "content.html")

def search(request):
    return render(request, "search.html")

def history(request):
    return render(request, "history.html")