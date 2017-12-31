from celery import Celery
from celery.schedules import crontab
from .models import Entry
import pt.fetcher as f


app = Celery()


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Executes every day at 23:00
    sender.add_periodic_task(
        # crontab(hour=23, minute=00),
        crontab(),
        update_price_data.s(),
    )


@app.task
def update_price_data():
    entries = Entry.objects.order_by('date_updated')
    for entry in entries:
        price, date = f.get_price_data(entry.url)
        if not price:
            continue
        if price != entry.price:
            entry.prices += ", ".format(entry.price)
            entry.trend = entry.TREND_DOWN if price < entry.price else entry.TREND_UP
            entry.price = price
