#!/usr/bin/python3
import importlib.util
import sys

if __name__ == "__main__":
    pyc_file_path = './hidden_4.pyc'

    spec = importlib.util.spec_from_file_location("hidden_4", pyc_file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules["hidden_4"] = module
    spec.loader.exec_module(module)

    if hasattr(module, 'my_secret_santa'):
        print("my_secret_santa")

    if hasattr(module, 'print_school'):
        print("print_school")

    if hasattr(module, 'print_hidden'):
        print("print_hidden")
