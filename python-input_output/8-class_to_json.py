#!/usr/bin/python3
"""Adds all command line arguments to a Pyfile."""

import json

def class_to_json(obj):
    """Adds all command line arguments to a Pyfile."""
    return json.dumps(obj.__dict__)
