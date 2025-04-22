from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include('app_spendings.urls')),
    path('auth/', include('app_auth.urls')),
    path('sections/', include('app_sections.urls')),
    path('admin/', admin.site.urls),
]