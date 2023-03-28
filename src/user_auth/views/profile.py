from __future__ import annotations

from typing import TYPE_CHECKING

from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from group_management.serializers.user_type import UserTypeSerializer

if TYPE_CHECKING:
    from rest_framework.authtoken.admin import User


class Profile(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs) -> Response:
        user: User = Token.objects.get(key=request.auth.key).user
        user_type_serializer: UserTypeSerializer = UserTypeSerializer(
            data={"user": user.pk, "group_type": user.poke_type.all().values_list("pk")}
        )
        user_type_serializer.is_valid()
        return Response(user_type_serializer.data, status=status.HTTP_200_OK)
