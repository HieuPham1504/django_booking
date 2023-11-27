from django.db import models
from ms_property.models import MsProperty

class MsPropertyCondition(models.Model):
    property = models.ForeignKey(MsProperty, on_delete=models.CASCADE, null=True, blank=True)
    icon = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=255)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.title
