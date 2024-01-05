from django.db import models
from ms_destination.models import MsDestination

class MsProperty(models.Model):
  destination_id = models.ForeignKey(MsDestination, on_delete=models.CASCADE)
  name = models.CharField(max_length=255, null=False)
  max_adults = models.IntegerField()
  max_childs = models.IntegerField()
  property_size = models.IntegerField()
  property_standard_price = models.FloatField()
  property_price_monday = models.FloatField()
  property_price_tuesday = models.FloatField()
  property_price_wednesday = models.FloatField()
  property_price_thursday = models.FloatField()
  property_price_friday = models.FloatField()
  property_price_saturday = models.FloatField()
  property_price_sunday = models.FloatField()
  image = models.ImageField(upload_to='images/')
  description = models.TextField(default=False, null=True)
  included_benefits = models.TextField(null=True, blank=True)
  other_services = models.TextField(null=True, blank=True)
  address = models.TextField(null=True, blank=True)
  total_size = models.FloatField(blank=True, null=True)
  rest_room_number = models.IntegerField(blank=True, null=True)
  bedroom_number = models.IntegerField(blank=True, null=True)
  location_iframe = models.TextField(blank=True, null=True)

  def __str__(self):
    return self.name