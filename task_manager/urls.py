from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),
    path('auth/', include('social_django.urls')),
    path('accounts/', include('allauth.urls'))# Google login
]


