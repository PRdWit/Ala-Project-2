"""
URL configuration for HOBO project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from HoboBrain import views
from HoboBrain.views import registreren, logout, inloggen

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('admin/', admin.site.urls),
    path('search/', views.search, name="search"),
    path('history/', views.history, name="history"),
    path('inloggen/', inloggen, name="inloggen"),
    path('logout/', logout, name="logout"),
    path('profile/', views.profile, name="profile"),
    path('registreren/', registreren, name="registreren"),
    path('<int:SerieID>/', views.serie_detail, name='serie_detail'),
    path("video/", views.video, name="video")
]
