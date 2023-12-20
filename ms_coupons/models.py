from django.db import models

class MsCoupon(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255, null=True, blank=True, unique=True)
    description = models.TextField()
    value = models.FloatField()
    date_start = models.DateField()
    date_end = models.DateField()
    image = models.ImageField(upload_to='coupons/', null=True, blank=True)
    sequence = models.IntegerField(default=1)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk:
            last_coupon = MsCoupon.objects.all().order_by('-id')
            last_coupon_id = 1 if len(last_coupon) == 0 else last_coupon[0].id + 1
            self.code = f'MSVOUCHER{last_coupon_id}'
        super(MsCoupon, self).save(*args, **kwargs)