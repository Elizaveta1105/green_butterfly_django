from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('app_spendings.urls')),
    path('auth/', include('app_auth.urls')),
    path('sections/', include('app_sections.urls')),
    path('admin/', admin.site.urls),
]