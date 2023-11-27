from django.contrib import admin
from .models import MsSocialMedia

class SocialMediaAdmin(admin.ModelAdmin):
    pass

admin.site.register(MsSocialMedia, SocialMediaAdmin)
