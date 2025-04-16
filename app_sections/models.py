from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum
from django.core.validators import MinValueValidator

class Section(models.Model):
    name = models.CharField(max_length=50)
    comment = models.CharField(max_length=200, blank=True)
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
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, db_index=True)

    def __str__(self):
        return self.name

    @classmethod
    def get_total_sum_uah(cls, user):
        return cls.objects.filter(user=user).aggregate(total=Sum('sum_uah'))['total'] or 0

    @classmethod
    def get_total_sum_currency(cls, user):
        total = cls.objects.filter(user=user).aggregate(total=Sum('sum_currency'))['total'] or 0
        return round(total, 2)

