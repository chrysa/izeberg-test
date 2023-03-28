from django.urls import path

from user_auth.views.auth import CustomAuthToken
from user_auth.views.profile import Profile

urlpatterns: list[path] = [
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('user/me/', Profile.as_view(), name='profile'),
]
