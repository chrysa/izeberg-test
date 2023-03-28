"""
poke-izeberg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from group_management.views.add_to_group import AddUserTypeGroup
from group_management.views.remove_to_group import RemoveUserTypeGroup
from user_auth.views import CustomAuthToken

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', CustomAuthToken.as_view()),
    path('api/group/<str:type_name>/add/', AddUserTypeGroup.as_view()),
    path('api/group/<str:type_name>/remove/', RemoveUserTypeGroup.as_view()),
]
