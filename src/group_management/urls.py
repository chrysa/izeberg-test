from django.urls import path

from group_management.views.add_to_group import AddUserTypeGroup
from group_management.views.remove_to_group import RemoveUserTypeGroup

urlpatterns: list[path] = [
    path('<str:type_name>/add/', AddUserTypeGroup.as_view()),
    path('<str:type_name>/remove/', RemoveUserTypeGroup.as_view()),
]
