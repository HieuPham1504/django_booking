from datetime import datetime
from django.db import models

class MsMapstarContact(models.Model):
    fullname = models.CharField(max_length=255, null=False)
    phone_number = models.CharField(max_length=20, null=False)
    email = models.EmailField(max_length=255, null=False)
    request = models.TextField(null=True, blank=True)
    create_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.fullname