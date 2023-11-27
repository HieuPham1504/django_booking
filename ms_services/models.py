from django.db import models
from ms_property.models import MsProperty

class MsServices(models.Model):
    name = models.CharField(max_length=255)
    property_id = models.ForeignKey(MsProperty, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField()
    price = models.FloatField(default=0, blank=True, null=True)
    is_extra = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.name
