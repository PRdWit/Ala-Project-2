from django.contrib.auth import login, authenticate
from django.shortcuts import render, get_object_or_404, redirect
from django_tables2 import RequestConfig
from HoboBrain.tables import streamTable
from HoboBrain.models import Serie, Klant, Genre, Abonnement, Aflevering, Seizoen, Stream
from django.db.models import Q
from django.contrib import messages
from django.db import connection
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import LogoutView
from HoboBrain.forms import RegistrationForm
from datetime import datetime, timedelta
import hashlib

# Handles the request to display the homepage. It retrieves data for active, trending, and editor's pick series. 
# It also retrieves the series the user has streamed and adds image filenames to the series data to render on the homepage.
def homepage(request):
    klant_id = request.session.get('klant_id')
    active_series = Serie.objects.filter(actief=True)
    trending_series = Serie.objects.filter(trending=True)
    editor_series = Serie.objects.filter(editorpick=True)

    with connection.cursor() as cursor:
            cursor.execute("SELECT DISTINCT serie.SerieID, serie.SerieTitel FROM stream RIGHT JOIN aflevering ON stream.AflID = aflevering.AfleveringID RIGHT JOIN seizoen ON aflevering.SeizID = seizoen.SeizoenID RIGHT JOIN serie ON seizoen.SerieID = serie.SerieID WHERE KlantID = %s;", [klant_id])
            user_streams = cursor.fetchall()

    user_streams_dicts = [
        {'serieid': row[0], 'serietitel': row[1]} for row in user_streams
    ]

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

    user_streams_with_images = [
        {'serie': serie, 'image_name': f'{str(serie["serieid"]).zfill(5)}.jpg'}
        for serie in user_streams_dicts
    ]

    context = {
        'series_with_images': series_with_images,
        'trending_series_with_images' : trending_series_with_images,
        'editor_series_with_images' : editor_series_with_images,
        'user_streams_with_images' : user_streams_with_images
    }

    return render(request, "homepage.html", context)

# Handles profile-related requests, such as updating user information. 
# If the request method is POST, it updates user information in the database. 
# Otherwise, it retrieves user information and renders the profile page with user data and options for updating information.
def profile(request):
    klant_id = request.session.get('klant_id')

    if request.method == "POST":
        voornaam = request.POST.get('voornaam')
        email = request.POST.get('email')
        password = request.POST.get('password')
        genre = request.POST.get('genre')
        aboID = request.POST.get('aboID')

        hashed_password = None
        if password:
            hashed_password = hashlib.sha256(password.encode()).hexdigest()

        with connection.cursor() as cursor:
            if hashed_password:
                cursor.execute(
                    "UPDATE klant SET voornaam = %s, email = %s, password = %s, genre = %s, aboID = %s WHERE klantnr = %s",
                    [voornaam, email, hashed_password, genre, aboID, klant_id]
                )
            else:
                cursor.execute(
                    "UPDATE klant SET voornaam = %s, email = %s, genre = %s, aboID = %s WHERE klantnr = %s",
                    [voornaam, email, genre, aboID, klant_id]
                )

        request.session['voornaam'] = voornaam

        return redirect('/profile')

    else:
        genres = Genre.objects.all()
        aboIDs = Abonnement.objects.all()

        with connection.cursor() as cursor:
            cursor.execute("SELECT voornaam, email, genre, aboID FROM klant WHERE klantnr = %s", [klant_id])
            klant = cursor.fetchone()
        
        return render(request, "profile.html", {
            "voornaam": klant[0],
            "email": klant[1],
            "genre": klant[2],
            "aboID": klant[3],
            "genres": genres,
            "aboIDs": aboIDs
        })
    
# Handles the search functionality. It retrieves the search term from the request's GET parameters. 
# Then, it queries the database for series matching the search term, if provided. 
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
    klant_id = request.session.get('klant_id')

    query1 = """
        SELECT DATE(d_start) AS day,
               SEC_TO_TIME(SUM(TIMESTAMPDIFF(SECOND, d_start, d_eind))) AS total_time 
        FROM stream 
        WHERE KlantID = %s 
        GROUP BY DATE(d_start);
    """
    
    query2 = """
        SELECT serie.SerieTitel,
               SEC_TO_TIME(SUM(aflevering.duur)) AS total 
        FROM stream 
        RIGHT JOIN aflevering ON stream.AflID = aflevering.AfleveringID 
        RIGHT JOIN seizoen ON aflevering.SeizID = seizoen.SeizoenID 
        RIGHT JOIN serie ON seizoen.SerieID = serie.SerieID 
        WHERE stream.KlantID = %s 
        GROUP BY serie.SerieTitel;
    """

    with connection.cursor() as cursor:
        cursor.execute(query1, [klant_id])
        results1 = cursor.fetchall()
        
        cursor.execute(query2, [klant_id])
        results2 = cursor.fetchall()

    data1 = [{'day': row[0], 'total_time': str(row[1])} for row in results1]
    data2 = [{'serie_title': row[0], 'total': str(row[1])} for row in results2]

    return render(request, "history.html", {"data1": data1, "data2": data2})

# Handles the user's viewing history. It retrieves the user's ID from the session. 
# Then, it executes two SQL queries to gather data about the user's streaming history.
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

# Manages the user login functionality. 
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
    

# Decorator function to enforce user authentication. 
# It checks if the user is logged in by verifying the presence of 'klant_id' in the session. 
# If not, it redirects the user to the login page. 
# Otherwise, it allows access to the requested view function.
def custom_login_required(view_func):
    def _wrapped_view_func(request, *args, **kwargs):
        if 'klant_id' not in request.session:
            return redirect('inloggen')
        return view_func(request, *args, **kwargs)
    return _wrapped_view_func

# Handles user logout functionality. 
def logout(request):
    if 'klant_id' in request.session:
        del request.session['klant_id']
    if 'klant_voornaam' in request.session:
        del request.session['klant_voornaam']
    return redirect('inloggen')

# Retrieves the details of a specific TV series based on the provided SerieID. 
def serie_detail(request, SerieID):
    serie = get_object_or_404(Serie, pk=SerieID)
    imbdlink = serie.imdblink
    image = f'{str(serie.serieid).zfill(5)}.jpg'

# It retrieves the necessary data from the request and inserts a new stream record into the database.
    if request.method == "POST":
        klantid = request.session.get('klant_id')
        afleveringid = request.POST.get('afleveringid')
        starttime = datetime.now()
        with connection.cursor() as cursor:
            cursor.execute("SELECT aflevering.Duur FROM stream RIGHT JOIN aflevering ON stream.AflID = aflevering.AfleveringID WHERE aflevering.AfleveringID = %s", [afleveringid])
            aflduration = cursor.fetchone()

        duration = timedelta(minutes = aflduration[0])
        endtime = starttime+duration

        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO stream (klantid, aflid, d_start, d_eind)"
                "VALUES (%s, %s, %s, %s)",
                [klantid ,afleveringid, starttime, endtime]
            )
        return redirect("homepage")
    
    # Retrieves genre information and related seasons of the series from the database.
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT genre.GenreNaam FROM genre INNER JOIN serie_genre ON genre.GenreID = serie_genre.GenreID WHERE serie_genre.SerieID = %s;",
            [SerieID]
        )
        genres = [row[0] for row in cursor.fetchall()]

        seizoenen = Seizoen.objects.filter(serieid=SerieID).prefetch_related('aflevering_set')

    context = {
        'serie': serie,
        'imbdlink': imbdlink,
        'genres': genres,
        'image_name': image,
        'seasons': seizoenen
    }
    return render(request, 'streampage.html', context)
