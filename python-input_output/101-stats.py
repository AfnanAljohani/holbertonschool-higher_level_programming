#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics."""
import sys


def print_stats(size, codes):
    """Print the accumulated file size and status code counts."""
    print("File size: {}".format(size))
    for code in sorted(codes):
        if codes[code]:
            print("{}: {}".format(code, codes[code]))


if __name__ == "__main__":
    size = 0
    codes = {"200": 0, "301": 0, "400": 0, "401": 0,
             "403": 0, "404": 0, "405": 0, "500": 0}
    count = 0

    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) >= 2:
                try:
                    size += int(parts[-1])
                except (ValueError, IndexError):
                    pass
                if parts[-2] in codes:
                    codes[parts[-2]] += 1
            count += 1
            if count % 10 == 0:
                print_stats(size, codes)
        print_stats(size, codes)
    except KeyboardInterrupt:
        print_stats(size, codes)
        raise
