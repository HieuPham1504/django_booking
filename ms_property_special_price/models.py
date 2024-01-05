from django.db import models
from ms_property.models import MsProperty

class MsPropertySpecialPrice(models.Model):
    is_active = models.BooleanField(default=True)
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.IntegerField()
    property = models.ForeignKey(MsProperty, on_delete=models.CASCADE)
