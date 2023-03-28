from __future__ import annotations

from typing import TYPE_CHECKING

from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from poke_api_accessor import PokeAccess

if TYPE_CHECKING:
    from rest_framework.authtoken.admin import User


class PokeList(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs) -> Response:
        available_pokemon_by_type: dict[str, list[str]] = {}
        poke_access: PokeAccess = PokeAccess()
        user: User = Token.objects.get(key=request.auth.key).user
        for poke_type in user.poke_type.all():
            for group_type in poke_type.group_type.all():
                type_name: str = group_type.type_name
                available_pokemon_by_type[type_name] = poke_access.get_pokemon_list_by_type(type_name=type_name)
        return Response(available_pokemon_by_type, status=status.HTTP_200_OK)
