from django.conf import settings
from django.db import models


class Account(models.Model):
    username = models.CharField(max_length=50, null=False, blank=False)
    email = models.CharField(max_length=70, null=False, blank=False)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.username
