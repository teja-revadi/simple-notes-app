from django.contrib import admin
from django.urls import path, include
from . import swagger

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('notes.urls')),
    path('', include(swagger)),
]
