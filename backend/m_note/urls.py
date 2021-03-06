from django.contrib import admin
from django.urls import path, include, re_path

from django.views.static import serve as _serve

def serve(request, path):
    if "." not in path:
        path = "index.html"
    return _serve(request, path, "/vue")

urlpatterns = [
    path('api/notes/', include('notes.urls')),
    path('api/users/', include('user.urls')),
    
    path('admin/', admin.site.urls),

    re_path(r'(?P<path>(^/?$|.*\.(js|css)))', serve),
    re_path(r'(?P<path>(^login/?$|.*\.(js|css)))', serve),
    re_path(r'(?P<path>(^registration/?$|.*\.(js|css)))', serve),
]
