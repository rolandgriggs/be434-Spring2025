#!/usr/bin/env python3
"""
Author : Xavier Griggs
Date   : 2025-02-02
Purpose: Print greeting
"""

import argparse


# --------------------------------------------------
def get_args():
                    """Get command-line arguments"""

                    parser = argparse.ArgumentParser(
                        description='Print greeting',
                        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

                    parser.add_argument('-g',
                                        '--greeting',
                                        metavar='str',
                                        type=str,
                                        default='Howdy',
                                        help='The greeting (default: Howdy)')

                    parser.add_argument(
                        '-n',
                        '--name',
                        metavar='str',
                        type=str,
                        default='Stranger',
                        help='Whom to greet (default: Stranger)')

                    parser.add_argument(
                        '-e',
                        '--excited',
                        action='store_true',
                        help='Include an exclamation point (default: False)')

                    return parser.parse_args()


# --------------------------------------------------
def main():
                    """Generate and print greeting"""

                    args = get_args()
                    greeting = f"{args.greeting}, {args.name}"
                    if args.excited:
                                        greeting += '!'
                    else:
                                        greeting += '.'

                    print(greeting)


# --------------------------------------------------
if __name__ == '__main__':
                    main()
