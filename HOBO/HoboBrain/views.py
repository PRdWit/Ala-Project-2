from django.shortcuts import render
from HoboBrain.models import Serie

# Create your views here.

def homepage(request):
    active_series = Serie.objects.filter(actief=True)
    context = {
        'active_series': active_series
    }
    return render(request, "homepage.html", context)

def profile(request):
    return render(request, "profile.html")
