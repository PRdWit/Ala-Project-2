from django.contrib.auth import login, authenticate
from django.shortcuts import render, get_object_or_404, redirect
from HoboBrain.models import Serie, Klant, Genre, Abonnement, Aflevering, Seizoen
from django.db.models import Q
from django.contrib import messages
from django.db import connection
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView
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

def registreren(request): 
    if request.method == "POST":
        voornaam = request.POST.get('voornaam')
        tussenvoegsel = request.POST.get('tussenvoegsel')
        achternaam = request.POST.get('achternaam')
        email = request.POST.get('email')
        password = request.POST.get('password')
        genre = request.POST.get('genre')
        aboID = request.POST.get('aboID')

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
        genres = Genre.objects.all()
        aboIDs = Abonnement.objects.all()


    return render(request, "registreren.html", {"form": form, "genres": genres, "aboIDs": aboIDs})

def inloggen(request):
    if request.method == 'POST':
        voornaam = request.POST.get('username')
        password = request.POST.get('password')
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        try:
            klant = Klant.objects.get(voornaam=voornaam, password=hashed_password)
            request.session['klant_id'] = klant.klantnr
            request.session['voornaam'] = klant.voornaam
            return redirect('/')
        except Klant.DoesNotExist:
            error_message = "Invalid username or password"
            return render(request, 'inloggen.html', {'error_message': error_message})
    else:
        return render(request, 'inloggen.html')
    

def custom_login_required(view_func):
    def _wrapped_view_func(request, *args, **kwargs):
        if 'klant_id' not in request.session:
            return redirect('inloggen')
        return view_func(request, *args, **kwargs)
    return _wrapped_view_func

def logout(request):
    if 'klant_id' in request.session:
        del request.session['klant_id']
    if 'klant_voornaam' in request.session:
        del request.session['klant_voornaam']
    return redirect('inloggen')


# Logout view
#class CustomLogoutView(LogoutView):
    #next_page = reverse_lazy("login")

def serie_detail(request, SerieID):
    serie = get_object_or_404(Serie, pk=SerieID)
    imbdlink = serie.imdblink
    image = f'{str(serie.serieid).zfill(5)}.jpg'

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT genre.GenreNaam FROM genre INNER JOIN serie_genre ON genre.GenreID = serie_genre.GenreID WHERE serie_genre.SerieID = %s;",
            [SerieID]
        )
        genres = [row[0] for row in cursor.fetchall()]

        seizoenen = Seizoen.objects.filter(serieid=SerieID).prefetch_related('aflevering_set')

        # afleveringen = Aflevering.objects.filter(seizid_id=SerieID)


    context = {
        'serie': serie,
        'imbdlink': imbdlink,
        'genres': genres,
        'image_name': image,
        'seasons': seizoenen
    }
    return render(request, 'streampage.html', context)
