from django.contrib import admin

from group_management.models.type_group import TypeGroup
from group_management.models.user_type import UserType

# Register your models here.
admin.site.register(TypeGroup)
admin.site.register(UserType)