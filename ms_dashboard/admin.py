from django.contrib import admin
from .models import MsMapstarContact

class MsMapstarContactAdmin(admin.ModelAdmin):
    pass

admin.site.register(MsMapstarContact, MsMapstarContactAdmin)
