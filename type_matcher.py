import datetime
import re


def is_string(data):
    return data.strip() != ""


def is_number(data):
    try:
        float(data)
        return True
    except ValueError:
        return False


def is_integer(data):
    try:
        int(data)
        return True
    except ValueError:
        return False


def is_date(x):
    try:
        datetime.datetime.strptime(x, '%d.%m.%Y')
        return True
    except ValueError:
        return False


def is_name(x):
    return is_string(x)


type_database = {
    "string": lambda x: is_string(x),
    "integer": lambda x: is_integer(x),
    "number": lambda x: is_number(x),
    "date": lambda x: is_date(x),
    "name": lambda x: is_name(x)
}


def match_type(element_type, data):
    return type_database[element_type](data)
