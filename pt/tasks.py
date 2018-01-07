# from celery.schedules import crontab
from .models import Entry
from .models import Price
from price_tracker.celery import app
import pt.fetcher as f


# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     # Executes every day at 23:00
#     sender.add_periodic_task(
#         # crontab(hour=23, minute=00),
#         crontab(),
#         update_price_data.s(),
#     )


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
