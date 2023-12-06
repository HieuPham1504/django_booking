from django.db import models

class MsCommonQuestion(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
