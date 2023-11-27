from django.db import models

class MsPaymentMethod(models.Model):
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name