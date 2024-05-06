from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request, "homepage.html")

def profile(request):
    return render(request, "profile.html")
