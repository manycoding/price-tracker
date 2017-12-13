import price_tracker as t


def test_get_price():
    price = t.get_price(
        "https://www.hanchor.com/products/Outdoor%20Series/MARBLE_Hiking_Backpack?locale=en", "NT$", "li")
    assert int(price) > 0, "Returned price is {}".format(price)


def test_price_not_found():
    price = t.get_price(
        "https://www.hanchor.com/products/Outdoor%20Series/MARBLE_Hiking_Backpack?locale=en", "NT$", "li3")
    assert price is None, "Returned price is {}, should be None".format(
        price)
