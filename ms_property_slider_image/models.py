from django.db import models
from ms_property.models import MsProperty

class MsPropertySliderImage(models.Model):
  property_id = models.ForeignKey(MsProperty, on_delete=models.CASCADE)
  image = models.ImageField(upload_to='property-slider/')

  def __str__(self):
    return self.property_id.name
