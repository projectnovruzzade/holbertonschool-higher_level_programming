#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics:
- Total file size
- Number of lines by status code
Prints metrics every 10 lines or on keyboard interruption.
"""

import sys

# List of allowed status codes
status_codes = [200, 301, 400, 401, 403, 404, 405, 500]


def print_metrics(total_size, status_dict):
    """Print metrics in checker-friendly format"""
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

            # Extract numbers from line (status and size)
            try:
                numbers = [int(s) for s in line.split() if s.isdigit()]
                if len(numbers) < 2:
                    continue
                status = numbers[-2]
                size = numbers[-1]
            except ValueError:
                continue

            # Count status codes
            if status in status_codes:
                status_dict[status] = status_dict.get(status, 0) + 1

            # Sum file size
            total_size += size
            line_count += 1

            # Print metrics every 10 lines
            if line_count % 10 == 0:
                print_metrics(total_size, status_dict)

    except KeyboardInterrupt:
        pass
    finally:
        # Always print final metrics
        print_metrics(total_size, status_dict)


if __name__ == "__main__":
    main()
