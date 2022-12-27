from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("home",views.home),
    path("initiatives",views.initiative),
    path("gallery",views.gallery),
    path("homeimages",views.homeimages),
    path("patronages",views.patronages),
    path("vision",views.vision),
    path("team",views.team),
    path("query",views.queries),
]