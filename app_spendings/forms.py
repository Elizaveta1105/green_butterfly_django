from django.forms import ModelForm, CharField, TextInput, FileInput

from .models import Picture, Spending
from cloudinary.forms import CloudinaryFileField


class PictureForm(ModelForm): # form validation
    description = CharField(max_length=300, min_length=5, widget=TextInput(attrs={"class": "form-control",
                                                                                  "id": "descriptionInput"}))
    image = CloudinaryFileField(widget=FileInput(attrs={"class": "form-control"}))

    class Meta:
        model = Picture
        exclude = ['user', 'spending']


class SpendingForm(ModelForm):
    class Meta:
        model = Spending
        exclude = ['user', 'section', 'sum_currency']