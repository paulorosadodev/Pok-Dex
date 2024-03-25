from django.contrib import admin
from django.urls import path
from pokedex import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pokemons/', views.pokemons, name="pokemons"),
    path('pokemon/<str:numero>', views.pokemon, name="pokemon"),
]
