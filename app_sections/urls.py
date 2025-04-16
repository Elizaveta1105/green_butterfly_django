from django.urls import path
from . import views
from . import apps

app_name = apps.AppSectionsConfig.name

urlpatterns = [
    path('', views.get_sections, name='sections'),
    path('create/', views.create_section, name='create-section'),
    path('<int:section_id>/edit', views.edit_section, name='edit-section'),
    path('<int:section_id>/delete', views.delete_section, name='delete-section')
]