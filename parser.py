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


def find_by_text(soup, text, tag, **kwargs):
    """
    Find the tag in soup that matches all provided kwargs, and contains the
    text.

    If no match is found, return None.
    If more than one match is found, raise ValueError.
    """
    elements = soup.find_all(tag, **kwargs)

    matches = []
    for element in elements:
        if element.find(text=like(text)):
            matches.append(str(element))
    if len(matches) > 1:
        raise ValueError("Too many matches:\n" + "\n".join(matches))
    elif len(matches) == 0:
        print("Nothing found with {} text, {} tag and {}".format(text, tag, kwargs))
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

    # matches = []
    # for element in elements:
    #     if element.find(text=like(text)):
    #         matches.append(element)
    if len(matches) > 1:
        raise ValueError("Too many matches:\n" + "\n".join(matches))
    elif len(matches) == 0:
        return None
    else:
        return matches[0]


def get_number_from_string(string):
    matches = re.findall(r'\d+', string)
    if len(matches) > 1:
        raise ValueError("Too many matches:\n" + "\n".join(matches))
    elif len(matches) == 0:
        return None
    else:
        return matches[0]
