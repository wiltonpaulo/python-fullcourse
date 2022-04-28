#!/usr/bin/env python3

import argparse
import sys

# build parser
parser = argparse.ArgumentParser(
    description="This script reads a file and prints each line in reverse order"
)

# parse the arguments
parser.add_argument("filename", help="the file to read")
parser.add_argument(
    "--normal", "-n", action="store_true", help="print lines with normal mode"
)
parser.add_argument("--limit", "-l", type=int, help="the number of line to read")
parser.add_argument("--version", "-v", action="version", version="%(prog)s 1.0")
args = parser.parse_args()

# do something
print(args)

try:
    with open(args.filename) as f:
        lines = f.readlines()
        lines.reverse()

        if args.limit:
            lines = lines[: args.limit]

        for line in lines:
            if args.normal:
                print(line.strip())
            else:
                print(line.strip()[::-1])
except FileNotFoundError as err:
    print(f"Error: {err}")
    sys.exit(2)
