from __future__ import annotations

from typing import TYPE_CHECKING

from rest_framework import serializers
from rest_framework import status

from group_management.models.user_type import UserType
from pokemon.models.type_group import TypeGroup

if TYPE_CHECKING:
    from typing import Any
    from typing import NoReturn


class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserType
        fields = ['user', 'group_type']

    def validate(self, data: dict[str, Any]) -> NoReturn | dict[str, str]:
        if UserType.objects.filter(user=data.get('user').pk, group_type__in=data.get('group_type')).exists():
            raise serializers.ValidationError(
                f"user {data.get('user')} already have type {data.get('group_type')[0].type_name}"
            )
        return data

    def save(self) -> tuple[status, UserType]:
        http_status: status
        instance, created = UserType.objects.get_or_create(user=self.validated_data["user"])
        for group in self.validated_data["group_type"]:
            group_instance, _ = TypeGroup.objects.get_or_create(type_name=group)
            instance.group_type.add(group_instance)
        instance.save()
        if created:
            http_status = status.HTTP_200_OK
        else:
            http_status = status.HTTP_201_CREATED
        return http_status, instance
