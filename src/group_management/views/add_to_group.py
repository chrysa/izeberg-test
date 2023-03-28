from __future__ import annotations

from typing import TYPE_CHECKING

from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from group_management.models.user_type import UserType
from group_management.serializers.type_group import TypeGroupSerializer
from group_management.serializers.user_type import UserTypeSerializer

if TYPE_CHECKING:
    from group_management.models.type_group import TypeGroup
    from django.contrib.auth.models import User


class AddUserTypeGroup(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, type_name: str, format=None) -> Response:
        http_status: status = status.HTTP_400_BAD_REQUEST
        value: dict[str, str]
        type_group_serializer: TypeGroupSerializer = TypeGroupSerializer(data={"type_name": type_name})
        if type_group_serializer.is_valid():
            type_group: TypeGroup = type_group_serializer.save()
            user: User = Token.objects.get(key=request.auth.key).user
            user_type_serializer: UserTypeSerializer = UserTypeSerializer(
                data={
                    "user": user.pk,
                    "group_type": [
                        type_group.pk,
                    ],
                }
            )
            if user_type_serializer.is_valid(raise_exception=True):
                http_status, _ = user_type_serializer.save()
                value = {"user": user.username, "type_name": type_name}
            else:
                value = type_group_serializer.errors
        else:
            value = type_group_serializer.errors
        return Response(value, status=http_status)
