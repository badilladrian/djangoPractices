
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('POST.urls')),
    path('admin/', admin.site.urls),
    path('posts', include('POST.urls')),
    ]
