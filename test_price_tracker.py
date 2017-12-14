import price_tracker as t


def test_get_price():
    price = t.get_price(
        "https://www.hanchor.com/products/Outdoor%20Series/MARBLE_Hiking_Backpack?locale=en")
    assert int(price) > 0, "Returned price is {}".format(price)


def test_price_not_found():
    price = t.get_price(
        "https://www.ozon.ru/context/detail/id/138860340/")
    assert price is None, "Returned price is {}, should be None".format(
        price)


def test_get_price_by_text():
    price = t.get_price(
        "https://www.aliexpress.com/item/TOAKS-Titanium-Pot-Camping-Cooking-Pots-Picnic-Hang-Pot-Ultralight-Titanium-Pot-1600ml-POT-1300-BH/32783166417.html")
    assert float(price) > 0, "Returned price is {}".format(price)

