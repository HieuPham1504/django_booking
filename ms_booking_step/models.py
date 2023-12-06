from django.db import models

class MsBookingStep(models.Model):
    sequence = models.IntegerField(unique=True)
    title = models.CharField(max_length=255)
    template_id = models.CharField(max_length=255)

    def __str__(self):
        return self.title
