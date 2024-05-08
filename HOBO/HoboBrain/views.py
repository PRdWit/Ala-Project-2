from django.shortcuts import render
from HoboBrain.models import Serie

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
