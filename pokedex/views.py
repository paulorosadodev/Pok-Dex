from django.shortcuts import render
from django.http import HttpResponse
from .models import Pokemon

tipos = [
    "Inseto",
    "Sombrio",
    "Dragão",
    "Elétrico",
    "Fada",
    "Lutador",
    "Fogo",
    "Voador",
    "Fantasma",
    "Planta",
    "Terrestre",
    "Gelo",
    "Normal",
    "Venenoso",
    "Psíquico",
    "Pedra",
    "Aço",
    "Água"
]

# Create your views here.
def pokemons(request):
    if request.method == 'GET':
        pokemons = Pokemon.objects.all()
        ctx = {
            'pokemons': pokemons,
            'tipos': tipos,
        }
        return render(request, 'pokemons.html', ctx)

def pokemon(request, numero):
    pokemon = Pokemon.objects.get(numero=numero)
    ctx = {
        'pokemon': pokemon
    }
    return render(request, 'pokemon.html', ctx)