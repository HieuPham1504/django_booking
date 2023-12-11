from django.db import models

class MsCoupon(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    description = models.TextField()
    value = models.FloatField()
    date_start = models.DateField()
    date_end = models.DateField()
    image = models.ImageField(upload_to='coupons/', null=True, blank=True)

    def __str__(self):
        return self.name