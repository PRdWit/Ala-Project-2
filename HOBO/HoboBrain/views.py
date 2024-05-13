from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from HoboBrain.models import Serie
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from HoboBrain.forms import RegistrationForm

def homepage(request):
    active_series = Serie.objects.filter(actief=True)
    trending_series = Serie.objects.filter(trending=True)
    editor_series = Serie.objects.filter(editorpick=True)

    series_with_images = [
        {'serie': serie, 'image_name': f'{str(serie.serieid).zfill(5)}.jpg'}
        for serie in active_series
    ]

    trending_series_with_images = [
        {'serie': serie, 'image_name': f'{str(serie.serieid).zfill(5)}.jpg'}
        for serie in trending_series
    ]

    editor_series_with_images = [
        {'serie': serie, 'image_name': f'{str(serie.serieid).zfill(5)}.jpg'}
        for serie in editor_series
    ]

    context = {
        'series_with_images': series_with_images,
        'trending_series_with_images' : trending_series_with_images,
        'editor_series_with_images' : editor_series_with_images
    }

    return render(request, "homepage.html", context)

def profile(request):
    return render(request, "profile.html")

def content(request):
    return render(request, "content.html")

def search(request):
    return render(request, "search.html")

def history(request):
    return render(request, "history.html")

def inloggen(request):
    return render(request, "inloggen.html")

def registreren(request): 
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect("/")  # Redirect to the homepage after registration
    else:
        form = RegistrationForm()

    return render(request, "registreren.html", {"form": form})

class CustomLoginView(LoginView):
    template_name = "inloggen.html"

# Logout view
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("login")