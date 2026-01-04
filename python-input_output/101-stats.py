#!/usr/bin/python3
"""
this is external
"""

import sys

status_codes = [200, 301, 400, 401, 403, 404, 405, 500]


def print_metrics(total_size, status_dict):
    """Prints the metrics in the required format."""
    print("File size: {}".format(total_size))
    for code in sorted(status_dict.keys()):
        print("{}: {}".format(code, status_dict[code]))


def main():
    total_size = 0
    status_dict = {}
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue

            parts = line.split()
            if len(parts) < 2:
                continue

            # Extract status code and file size
            try:
                status = int(parts[-2])
                size = int(parts[-1])
            except (ValueError, IndexError):
                continue

            if status in status_codes:
                status_dict[status] = status_dict.get(status, 0) + 1

            total_size += size
            line_count += 1

            if line_count % 10 == 0:
                print_metrics(total_size, status_dict)

    except KeyboardInterrupt:
        pass
    finally:
        print_metrics(total_size, status_dict)
