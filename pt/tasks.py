from .models import Entry
from .models import Price
from price_tracker.celery import app
import pt.fetcher as f


@app.task
def update_price_data():
    entries = Entry.objects.all()
    for entry in entries:
        price, date = f.get_price_data(entry.url)
        if not price:
            continue
        last_price = entry.price_set.last().price
        if price != last_price:
            price = Price(entry=entry, price=price, date=date)
            entry.trend = entry.TREND_DOWN if price < last_price else entry.TREND_UP
            entry.save()
            price.save
