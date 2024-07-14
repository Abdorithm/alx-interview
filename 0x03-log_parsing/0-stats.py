#!/usr/bin/python3
"""
Log parsing
"""
import sys


def print_stats(fileSize, statusCode):
    """Print the currenct stats"""
    print('File size: {}'.format(fileSize))
    for key, val in statusCode.items():
        if val != 0:
            print('{}: {}'.format(key, val))


fileSize = 0
statusCode = {
    '200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
    '404': 0, '405': 0, '500': 0
}

n_input = 0

try:
    for line in sys.stdin:
        ln = line.split()

        if len(ln) > 2:
            n_input += 1

            if n_input <= 10:
                fileSize += int(ln[-1])
                code = ln[-2]

                if (code in statusCode.keys()):
                    statusCode[code] += 1

            if (n_input == 10):
                print_stats(fileSize, statusCode)
                n_input = 0

finally:
    print_stats(fileSize, statusCode)
