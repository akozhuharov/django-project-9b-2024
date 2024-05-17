from django.db import models
from django.conf import settings


class Post(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
