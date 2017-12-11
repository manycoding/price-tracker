import json
import parser
import router
from bs4 import BeautifulSoup


def get_price(type, url, text, tag, **kwargs):
    """Get price value from url by path"""
    soup = BeautifulSoup(router.do_get(url).text, "html.parser")
    price_str = str(parser.find_by_text(soup, text, tag, **kwargs))
    price = parser.get_number_from_string(price_str)
    return price


def main():
    with open("input") as file:
        for line in file:
            type = line.split(',')[1]
            url, type, text, tag = line.split(',')
            price = get_price(type, url, text, tag)

            print("{}\t{}".format(url, price))


if __name__ == "__main__":
    main()
