#!/usr/bin/python3
class MyList(list):
    def __init__(self, *args):
        super().__init__(self, *args)

    def append(self, value):
        super().append(value)

    def print_sorted(self):
        print(sorted(self))

    def __str__(self):
        return f"{super().__str__()}"
