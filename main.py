import argparse
import price_tracker as t


def main(args):
    items = t.load_items(args.history_log)
    if items is None:
        items = list()
    items = t.update_price_data(items)
    if args.input_file:
        items = t.add_price_data(items, args.input_file)
    t.save_items(items, args.history_log)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-log", "--history_log", default="history_log", help="""
        File with previously tracked data
        """)
    parser.add_argument("-i", "--input_file", help="""
        Input file with data for items you want to track.
        Line format:
        text - url,type,text,tag
        tag - url,type,tag="value",tag2="value"
        Example:
        https://www.aliexpress.com/item/TOAKS-Titanium-Pot-Camping-Cooking-Pots-Picnic-Hang-Pot-Ultralight-Titanium-Pot-1600ml-POT-1300-BH/32783166417.html,tag,itemprop="price"
        """)
    args = parser.parse_args()
    main(args)
