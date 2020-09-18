from django.contrib import admin
from django.urls import path, include, re_path
from django.views.decorators.csrf import csrf_exempt
from django.views.static import serve as _serve

def serve(request, path):
    if "." not in path:
        path = "index.html"
    return _serve(request, path, "/vue")

urlpatterns = [
    path('api/', include('notes.urls')),
    path('admin/', admin.site.urls),
    re_path(r'(?P<path>(^/?$|.*\.(js|css)))', serve)
]
