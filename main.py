import notifications
import argparse
import price_tracker as t


def main(args):
    if args.test:
        items = list()
    else:
        items = t.load(args.history_log)
        if items is None:
            items = list()
        items, updated_items = t.update_price_data(items)

        settings = t.load(args.settings_file)
        if updated_items:
            notifications.send_email(settings["to"], settings["sender"],
                                     settings["pass"], updated_items)
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
    parser.add_argument("-t", "--test", action="store_true", help="""
        File with previously tracked data
        """)
    parser.add_argument("-s", "--settings_file", default="config", help="""
        File with email settings, one per line.
        From, To and Password.
        """)
    args = parser.parse_args()
    main(args)
