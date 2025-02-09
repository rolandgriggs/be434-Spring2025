#!/usr/bin/env python3
"""
Author : Xavier Griggs
Date   : 2025-02-09
Purpose: divide 2 numbers
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Divide two numbers',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('ints',
                        metavar='INT',
                        type=int,
                        nargs=2,
                        help='Numbers to divide')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Perform division"""

    args = get_args()
    num1, num2 = args.ints

    if num2 == 0:
        print('usage: divide.py [-h] INT INT', file=sys.stderr)
        print('divide.py: error: Cannot divide by zero, dum-dum!', file=sys.stderr)
        return 1

    print(f'{num1} / {num2} = {num1 // num2}')
    return 0


# --------------------------------------------------
if __name__ == '__main__':
   sys.exit(main())
