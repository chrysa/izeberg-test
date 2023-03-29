from __future__ import annotations

from typing import NoReturn

from rest_framework import serializers

from poke_api_accessor import PokeAccess
from pokemon.models.type_group import TypeGroup


class TypeGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeGroup
        fields = ["type_name"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.poke_access = PokeAccess()

    def validate_type_name(self, value: str) -> str | NoReturn:
        if value.lower() not in self.poke_access.type_list_name:
            raise serializers.ValidationError(f"Type `{value}` is not valid")
        return value.lower()

    def save(self) -> TypeGroup:
        instance: TypeGroup
        instance, _ = TypeGroup.objects.get_or_create(
            type_name=self.validated_data["type_name"],
            type_id=self.poke_access.get_type_id(poke_type=self.validated_data["type_name"]),
        )
        return instance
