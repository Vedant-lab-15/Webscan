from django.contrib import admin
from django.urls import path
from scanner.views import scan_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', scan_view, name='scanner'),
]
