from django.urls import path
from . import views
from . import apps

app_name = apps.AppSpendingsConfig.name

urlpatterns = [
    path('', views.home, name='home'),
    path('section/<int:section_id>/spendings', views.spendings, name='spendings'),
    path('section/<int:section_id>/add-spending', views.add_spending, name='add-spending'),
    path('section/<int:section_id>/spending/<int:spending_id>/edit', views.edit_spending, name='edit-spending'),
    path('spending/<int:spending_id>/remove', views.remove_spending, name='remove-spending'),
    path('spendings/<int:spending_id>/images', views.get_images, name='spending-images'),
    path('spendings/<int:spending_id>/upload', views.upload, name='upload'),
    path('spendings/<int:spending_id>/edit/<int:pic_id>', views.edit_image, name='edit_image'),
    path('images/remove/<int:pic_id>', views.remove_image, name='remove_image')
]