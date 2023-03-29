from django.urls import path

from pokemon.views.poke_list import PokeList
from pokemon.views.pokemon_acces import PokeAcces

urlpatterns: list[path] = [
    path("", PokeList.as_view(), name="get-available-pokemon-list"),
    path("<int:id>/", PokeAcces.as_view(), name="get-pokemon-by-id"),
    path("<str:name>/", PokeAcces.as_view(), name="get-pokemon-by-name"),
]
