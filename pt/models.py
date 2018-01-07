from django.db import models
from django.contrib.auth.models import User


class Entry(models.Model):
    """A URL entry of item which price user wants to track"""
    url = models.CharField(max_length=256)
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
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model"""
        if self.trend:
            return "{}\t{}".format(self.trend, self.url)
        return "{}".format(self.url)


class Price(models.Model):
    """History of price changes"""
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=False)

    class Meta:
        verbose_name_plural = 'prices'

    def __str__(self):
        """Return a string representation of the model"""
        return "{}\t{}".format(self.price, self.date)
