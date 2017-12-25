import json
import parser
import router
import os.path
from bs4 import BeautifulSoup
from datetime import datetime


def get_price(url):
    """Get price value from url by path"""
    r = router.do_get(url)
    if not r:
        return None
    soup = BeautifulSoup(r.text, "html.parser")
    return parser.find_price(soup)


def update_price_data(tracking_items):
    """Get current prices for saved items"""
    updated_items = []
    for item in tracking_items:
        price = get_price(item['url'])
        print("Fetched {} from {}".format(price, item['url']))

        if price is None:
            continue
        if price != item['price']:
            if 'prices' not in item:
                item['prices'] = [item['price']]
            elif 'prices' in item:
                if price != item['prices'][-1]:
                    item['prices'].append(item['price'])

            item['price'] = price
            item['timestamp'] = (str(datetime.utcnow())).split('.')[0]
            updated_items.append(item)

    return tracking_items, updated_items


def add_price_data(tracking_items, input_file):
    """Get current prices for new items"""
    with open(input_file) as file:
        for line in file:
            # Ignore commented lines
            if line.startswith("#"):
                continue
            url = line.strip()

            # Skip if url already exists
            if [i for i in tracking_items if i['url'] == url]:
                continue

            r = router.do_get(url)
            if not r:
                return None
            soup = BeautifulSoup(r.text, "html.parser")
            price = parser.find_price(soup)
            if price is None:
                continue
            print("Fetched {} from {}".format(price, url))
            tracking_items.append({
                "url": url,
                "price": price,
                "timestamp": (str(datetime.utcnow())).split('.')[0]
            })

    return tracking_items


def save_items(tracking_items, file):
    with open(file, "w") as history:
        json.dump(tracking_items, history)


def load(file):
    if not os.path.exists(file):
        return None
    with open(file, "r") as history:
        try:
            return json.load(history)
        except ValueError as err:
            print(err)
        else:
            return None
