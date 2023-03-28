from django.contrib.auth.models import User
from django.db import models

from group_management.models.type_group import TypeGroup


class UserType(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group_type = models.ManyToManyField(TypeGroup)
