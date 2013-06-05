from django.db import models


class Grain(models.Model):
    key = models.CharField(max_length=1024, unique=True, db_index=True)
    content_type = models.CharField(max_length=255, default='text/plain')
    value = models.TextField(blank=True)
