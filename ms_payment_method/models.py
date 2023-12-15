from django.db import models

class MsPaymentMethod(models.Model):
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='payment-method/', null=True, blank=True)
    main_QR_code_img = models.ImageField(upload_to='payment-method/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    sequence = models.IntegerField(default=100)

    def __str__(self):
        return self.name