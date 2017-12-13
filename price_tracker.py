import json
import parser
import router
import os.path
from bs4 import BeautifulSoup
from datetime import datetime


def get_price(url, text, tag, **kwargs):
    """Get price value from url by path"""
    r = router.do_get(url)
    if not r:
        return None
    soup = BeautifulSoup(r.text, "html.parser")
    price_str = str(parser.find_by_text(soup, text, tag, **kwargs))
    price = parser.get_number_from_string(price_str)
    return price


def update_price_data(tracking_items):
    """Get current prices for saved items"""
    for item in tracking_items:
        price = get_price(item['url'], item['text'], item['tag'])
        if price is None:
            continue
        if 'prices' in item and price != item['prices'][-1]:
            item['prices'].append(price)
            item['price'] = price
            item['timestamp'] = (str(datetime.utcnow())).split('.')[0]
    return tracking_items


def add_price_data(tracking_items, input_file):
    """Get current prices for new items"""
    with open(input_file) as file:
        for line in file:
            try:
                url, text, tag = line.rstrip().split(',')
            except ValueError as err:
                print(err)
                continue
            if [i for i in tracking_items if i['url'] == url]:
                continue
            price = get_price(url, text, tag)
            if price is None:
                continue
            print("Fetched {}\t{}".format(url, price))
            tracking_items.append({
                "url": url,
                "price": price,
                "text": text,
                "tag": tag,
                "timestamp": (str(datetime.utcnow())).split('.')[0]
            })

    return tracking_items


def save_items(tracking_items, file):
    with open(file, "w") as history:
        json.dump(tracking_items, history)


def load_items(file):
    if not os.path.exists(file):
        return None
    with open(file, "r") as history:
        try:
            return json.load(history)
        except ValueError as err:
            print(err)
        else:
            return None
