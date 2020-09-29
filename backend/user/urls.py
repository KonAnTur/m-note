from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path("registration/", views.UserCreate.as_view(), name="user_create"),
    path("authorization/", views.LoginView.as_view(), name="login"),
]

urlpatterns = format_suffix_patterns(urlpatterns)