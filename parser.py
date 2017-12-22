import re


MATCH_ALL = r'.*'


def like(string):
    """
    Return a compiled regular expression that matches the given
    string with any prefix and postfix, e.g. if string = "hello",
    the returned regex matches r".*hello.*"
    """
    string_ = string
    if not isinstance(string_, str):
        string_ = str(string_)
    regex = MATCH_ALL + re.escape(string_) + MATCH_ALL
    return re.compile(regex, flags=re.DOTALL)


def find_text_by_text(soup, text):
    """
    Find the tag in soup that contains the text.

    If no match is found, return None.
    If more than one match is found, raise ValueError.
    """
    matches = soup.find_all(text=lambda t:
                            re.compile(like(text)).match(t))

    print("Found {} items with {} text:".format(len(matches), text))
    # print(matches)
    matches = [get_number_from_string(t) for t in matches
               if get_number_from_string(t)]
    if len(matches) > 1:
        raise ValueError("Too many matches:\n" + "\n".join(matches))
    elif len(matches) == 0:
        return None
    else:
        return matches[0]


def find_by_attrs(soup, tag, **kwargs):
    """
    Find the tag in soup that matches all provided kwargs

    If no match is found, return None.
    If more than one match is found, raise ValueError.
    """
    matches = soup.find_all(tag, **kwargs)

    if len(matches) > 1:
        raise ValueError("Too many matches:\n" + "\n".join(matches))
    elif len(matches) == 0:
        return None
    else:
        return matches[0]


def find_text_by_attrs(soup, pattern):
    """
    Find the tag text in soup which attributes match provided pattern

    If more than one match is found, raise ValueError.
    """
    matches = soup.find_all(lambda t:
                            any(re.compile(pattern).
                                match(str(a)) for a in t.attrs.values()))
    print("Found {} items with {} pattern:".format(len(matches), pattern))
    # print(matches)
    matches = [get_number_from_string(
        e.text) for e in matches if get_number_from_string(e.text)]
    if len(matches) > 1:
        raise ValueError("Too many matches:\n" + "\n".join(matches))
    elif len(matches) == 0:
        return None
    else:
        return matches[0]


def get_number_from_string(string):
    """
    Get number from string
    """
    # Remove normal. non-breaking spaces &nbsp;
    string = string.replace(' ', '').replace(' ', '')

    matches = re.findall(r'\d+.\d+', string)
    if len(matches) > 1:
        raise ValueError("Too many matches:\n" + "\n".join(matches))
        return None
    elif len(matches) == 0:
        return None
    else:
        return matches[0]


def find_price(soup):
    """
    Price search strategy
    """
    price = find_text_by_attrs(soup, "(p|P)rice")
    if not price:
        price = find_text_by_text(soup, "NT$")

    # Normalize delimiter
    if price:
        price = price.replace(",", ".")
    return price


def xstr(s):
    """
    Return empty string if it's None
    """
    if s is None:
        return ""
    return str(s)
