from django.contrib.auth import login, authenticate
from django.shortcuts import render, get_object_or_404, redirect
from HoboBrain.models import Serie, Klant
from django.db.models import Q
from django.db import connection
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from HoboBrain.forms import RegistrationForm
import hashlib


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

def search(request):
    search_term = request.GET.get('query', '')

    all_series = Serie.objects.filter(actief=True)
    all_series_with_images = [{'serie': serie, 'image_name': f'{str(serie.serieid).zfill(5)}.jpg'} for serie in all_series]

    if search_term:
        results = Serie.objects.filter(Q(serietitel__icontains=search_term) & Q(actief=True))
        results_with_images = [{'serie': serie, 'image_name': f'{str(serie.serieid).zfill(5)}.jpg'} for serie in results]
    else:
        results_with_images = all_series_with_images

    context = {
        'search_term': search_term,
        'results_with_images': results_with_images,
    }

    return render(request, "search.html", context)


def history(request):
    return render(request, "history.html")

def inloggen(request):
    return render(request, "inloggen.html")

def registreren(request): 
    if request.method == "POST":
        voornaam = request.POST.get('voornaam')
        aboID = request.POST.get('aboID')
        tussenvoegsel = request.POST.get('tussenvoegsel')
        achternaam = request.POST.get('achternaam')
        email = request.POST.get('email')
        password = request.POST.get('password')
        genre = request.POST.get('genre')

        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO klant (aboID, voornaam, tussenvoegsel, achternaam, email, password, genre) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s)",
                [aboID ,voornaam, tussenvoegsel, achternaam, email, hashed_password, genre]
            )

        return redirect("inloggen")
    else:
        form = RegistrationForm()

    return render(request, "registreren.html", {"form": form})

class CustomLoginView(LoginView):
    template_name = "inloggen.html"

# Logout view
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("login")

def serie_detail(request, SerieID):
    serie = get_object_or_404(Serie, pk=SerieID)
    imbdlink = serie.imdblink

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT genre.GenreNaam FROM genre INNER JOIN serie_genre ON genre.GenreID = serie_genre.GenreID WHERE serie_genre.SerieID = %s;",
            [SerieID]
        )
        genres = [row[0] for row in cursor.fetchall()]


    context = {
        'serie': serie,
        'imbdlink': imbdlink,
        'genres': genres
    }
    return render(request, 'streampage.html', context)

#SELECT genre.GenreNaam
#FROM genre
#INNER JOIN serie_genre ON genre.GenreID = serie_genre.GenreID
#WHERE serie_genre.SerieID = <your_serie_id>;
