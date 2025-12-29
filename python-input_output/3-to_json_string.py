#!/usr/bin/python3
import json
"""
this is global enviroment
"""

def to_json_string(my_obj):
    data = my_obj
    return json.dumps(data)
