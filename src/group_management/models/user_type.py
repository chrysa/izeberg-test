from django.contrib.auth.models import User
from django.db import models

from pokemon.models.type_group import TypeGroup


class UserType(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="poke_type")
    group_type = models.ManyToManyField(TypeGroup)
