from django.contrib import admin
from django.urls import path, include
from main.views import load_frontend  # Import the view to load your frontend

urlpatterns = [
    path('', load_frontend, name='frontend'),
    path("", include('main.urls')),
    path('admin/', admin.site.urls),
]
