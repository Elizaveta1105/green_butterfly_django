from decimal import Decimal
from pathlib import Path
from uuid import uuid4

import requests
from cloudinary.models import CloudinaryField
from django.core.validators import MinValueValidator
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.db.models import Sum

from app_sections.models import Section


#TODO:   author = models.ForeignKey(Author, on_delete=models.SET_NULL, related_name="posts") + get_object_or_404

def validate_file_size(value):
    filesize = value.size

    if filesize > 1000000:
        raise ValidationError('Max size is 1MB')
    return value

def upload_image(instance, filename):
    upload_to = Path(instance.user.username) if instance.user else Path("images")
    extension = Path(filename).suffix
    new_filename = f"{uuid4().hex}{extension}"

    return str(upload_to/new_filename)

def get_usd_data():
    response = requests.post("https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5").json()
    data = list(filter(lambda item: item["ccy"] == "USD", response))

    return data


def covert_uah_to_usd(uah_amount):
    currency_data = get_usd_data()
    buy_rate = Decimal(currency_data[0]["buy"])
    usd_amount = Decimal(uah_amount) / buy_rate
    return usd_amount.quantize(Decimal("0.01"))

class Spending(models.Model):
    name = models.CharField(max_length=50)
    comment = models.CharField(max_length=200, blank=True, null=True)
    sum_uah = models.DecimalField(max_digits=15,
                                  decimal_places=2,
                                  default=0,
                                  validators=[MinValueValidator(0)]
    )
    sum_currency = models.DecimalField(max_digits=15,
                                       decimal_places=2,
                                       default=0,
                                       validators=[MinValueValidator(0)]
    )
    payment_date = models.DateField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, db_index=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, null=True, blank=True)

    @classmethod
    def get_total_sum_uah(cls, user, section_id):
        return cls.objects.filter(user=user, section=section_id).aggregate(total=Sum('sum_uah'))['total'] or 0

    @classmethod
    def get_total_sum_currency(cls, user, section_id):
        return cls.objects.filter(user=user, section=section_id).aggregate(total=Sum('sum_currency'))['total'] or 0

    @classmethod
    def get_total_count(cls, user, section_id):
        return cls.objects.filter(user=user, section=section_id).count()


class Picture(models.Model):
    description = models.CharField(max_length=300)
    image = CloudinaryField('image', overwrite=True)
    public_id = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    spending = models.ForeignKey(Spending, on_delete=models.CASCADE, null=True)