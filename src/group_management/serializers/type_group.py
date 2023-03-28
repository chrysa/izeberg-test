from __future__ import annotations

from typing import NoReturn
from typing import TYPE_CHECKING

import requests
from django.conf import settings
from rest_framework import serializers

from group_management.models.type_group import TypeGroup

if TYPE_CHECKING:
    from requests import request


def get_type_list() -> list[str] | NoReturn:
    response: request = requests.get(settings.POKE_API_TYPE)
    if response.json is None:
        raise Exception("POKE API don't return any types")
    else:
        return [value["name"].lower() for value in response.json()["results"]]


class TypeGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeGroup
        fields = ['type_name']

    def validate_type_name(self, value: str) -> str | NoReturn:
        if value.lower() not in get_type_list():
            raise serializers.ValidationError(f"Type `{value}` is not valid")
        return value.lower()

    def save(self) -> TypeGroup:
        instance, _ = TypeGroup.objects.get_or_create(type_name=self.validated_data["type_name"])
        return instance
