from django.contrib import admin
from .models import MsCertificate

class CertificateAdmin(admin.ModelAdmin):
    pass

admin.site.register(MsCertificate, CertificateAdmin)
