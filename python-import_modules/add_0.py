#!/usr/bin/python3
from add_0 import add  # Import the function normally

def main():
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))

# This block runs only if the file is executed directly
if __name__ == "__main__":
    main()