from django.db import models


class Grain(models.Model):
    key = models.CharField(max_length=1024, unique=True, db_index=True)
    content_type = models.CharField(max_length=255, default='text/plain')
    value = models.TextField(blank=True)

    def __unicode__(self):
        return u'{0} ({1}): {2!r}'.format(
            self.key, self.content_type, self.value[:100])
