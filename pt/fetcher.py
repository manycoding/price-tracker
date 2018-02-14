import pt.parser as parser
import pt.router as router
from bs4 import BeautifulSoup
from decimal import Decimal
from django.utils import timezone


def get_price_data(url):
    """Get current price data from url"""
    r = router.do_get(url)
    if not r:
        return None, timezone.now()
    soup = BeautifulSoup(r.text, "html.parser")
    price = parser.find_price(soup)
    if price is None:
        return None, timezone.now()
    print("Fetched {} from {}".format(price, url))
    return Decimal(price), timezone.now()
