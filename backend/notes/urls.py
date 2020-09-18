from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path("users/", csrf_exempt(views.UserCreate.as_view()), name="user_create"),
    path("login/", csrf_exempt(views.LoginView.as_view()), name="login"),

    path('notes/', views.NoteList.as_view()),
    path('notes/<int:pk>/', views.NotesDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)