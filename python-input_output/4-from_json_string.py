#!/usr/bin/python3
"""Returns the JSON representation of an object."""

import json


def from_json_string(my_str):
    data = my_str
    return json.loads(data)
