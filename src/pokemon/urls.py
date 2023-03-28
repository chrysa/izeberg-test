from django.urls import path

from pokemon.views.poke_list import PokeList

urlpatterns: list[path] = [path('', PokeList.as_view())]
