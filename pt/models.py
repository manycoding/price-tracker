from django.db import models


class Entry(models.Model):
    """A URL entry of item which price user wants to track"""
    url = models.CharField(max_length=256)
    date_updated = models.DateTimeField(auto_now_add=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    TREND_UP = "UP"
    TREND_DOWN = "DOWN"
    TREND_CHOICES = (
        (TREND_UP, '+'),
        (TREND_DOWN, '-'),
    )
    trend = models.CharField(
        max_length=4,
        choices=TREND_CHOICES,
        null=True
    )
    prices = models.CharField(max_length=10000, null=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model"""
        if self.trend:
            return "{} {}\t{}".format(self.price, self.trend, self.url)
        return "{}\t{}".format(self.price, self.url)
