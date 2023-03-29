from __future__ import annotations

from typing import Any
from typing import TYPE_CHECKING

from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from poke_api_accessor import PokeAccess

if TYPE_CHECKING:
    from group_management.models.user_type import UserType


class PokeAcces(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs) -> Response:
        http_status: status = status.HTTP_400_BAD_REQUEST
        poke: list[dict[str, Any]] = {}
        request_result: list[dict[str, Any]] = {}
        poke_access: PokeAccess = PokeAccess()
        available_types: list[UserType] = list(
            Token.objects.get(key=request.auth.key).user.poke_type.all().values_list("group_type__type_name", flat=True)
        )
        if "id" in kwargs.keys():
            request_result = poke_access.get_pokemon(pokemon=kwargs.get("id"))
        elif "name" in kwargs.keys():
            request_result = poke_access.get_pokemon(pokemon=kwargs.get("name"))
        if request_result:
            target_types: list[str] = [poke_type["type"]["name"] for poke_type in request_result["types"]]
            if any([type_test in target_types for type_test in available_types]):
                poke = request_result
                http_status = status.HTTP_200_OK
        return Response(poke, status=http_status)
