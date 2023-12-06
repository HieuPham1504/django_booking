from django.db import models

class MsCompany(models.Model):
  name = models.CharField(max_length=100, null=False)
  email = models.EmailField(max_length=255, null=True, blank=True)
  address = models.TextField(blank=True, null=True)
  description = models.TextField(null=True, blank=True)
  is_admin = models.BooleanField(default=False)
  phone = models.CharField(max_length=20, null=True, blank=True)
  zalo_link = models.CharField(max_length=255, null=True, blank=True)
  facebook_link = models.CharField(max_length=255, null=True, blank=True)
  tiktok_link = models.CharField(max_length=255, null=True, blank=True)
  youtube_link = models.CharField(max_length=255, null=True, blank=True)

  def __str__(self):
    return self.name