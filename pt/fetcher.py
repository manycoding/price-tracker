import pt.parser as parser
import pt.router as router
from bs4 import BeautifulSoup
from datetime import datetime


def get_price_data(url):
    """Get current price data from url"""
    r = router.do_get(url)
    if not r:
        return None
    soup = BeautifulSoup(r.text, "html.parser")
    price = parser.find_price(soup)
    if price is None:
        return -1, (str(datetime.utcnow())).split('.')[0]
    print("Fetched {} from {}".format(price, url))
    return price, (str(datetime.utcnow())).split('.')[0]
