from __future__ import annotations

from typing import TYPE_CHECKING

from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from group_management.models.user_type import UserType
from pokemon.models.type_group import TypeGroup
from pokemon.serializers.type_group import TypeGroupSerializer

if TYPE_CHECKING:
    from django.contrib.auth.models import User


class RemoveUserTypeGroup(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, type_name: str) -> Response:
        http_status: status = status.HTTP_400_BAD_REQUEST
        value: dict[str, str] = {}
        user: User = Token.objects.get(key=request.auth.key).user
        if UserType.objects.filter(
            user=user,
            group_type__type_name__in=[
                type_name,
            ],
        ).exists():
            type_group_serializer: TypeGroupSerializer = TypeGroupSerializer(data={"type_name": type_name})
            if type_group_serializer.is_valid():
                type_group: TypeGroup
                type_group = TypeGroup.objects.get(type_name=type_group_serializer.validated_data["type_name"])
                instance: UserType = UserType.objects.get(user=user)
                if type_group in instance.group_type.all():
                    instance.group_type.remove(type_group)
                    instance.save()
                    http_status: status = status.HTTP_200_OK
                else:
                    value = {"error": f"user {user.username} don't have type `{type_group.type_name}`"}
            else:
                value = type_group_serializer.errors
        else:
            value = {"error": f"user {user.username} don't have type `{type_name}`"}
        return Response(value, status=http_status)
