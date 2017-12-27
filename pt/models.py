from django.contrib.postgres.fields import JSONField
from django.db import models


class Entry(models.Model):
    """A URL entry of item which price user wants to track"""
    url = models.CharField(max_length=256)
    date_updated = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model"""
        return "{}\t{}".format(self.url, self.price)
