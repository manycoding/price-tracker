from .models import Entry
from .models import Price
import pt.fetcher as f


def update_price_data():
    entries = Entry.objects.all()
    for entry in entries:
        price, date = f.get_price_data(entry.url)
        if not price:
            continue
        last_price = entry.price_set.last().price
        if price != last_price:
            entry.trend = entry.TREND_DOWN if price < last_price else entry.TREND_UP
            entry.save()
            p = Price(entry=entry, price=price, date=date)
            p.save()
