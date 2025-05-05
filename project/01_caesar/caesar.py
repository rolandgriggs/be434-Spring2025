#!/usr/bin/env python3
"""
Author : Xavier Griggs
Date   : 2025-04-30
Purpose: Implement Caesar Shift Cipher for encoding and decoding text files
"""

import argparse
import os


# --------------------------------------------------
def shift_letter(letter, shift, decode=False):
    """Shift a single letter according to Caesar Cipher rules"""

    if letter.isalpha():
        letter = letter.upper()
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        idx = alpha.index(letter)

        if decode:
            shift = -shift

        new_idx = (idx + shift) % 26
        return alpha[new_idx]
    else:
        return letter


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Encode or decode a message using Caesar Shift Cipher',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        help='Input file to encode or decode',
                        type=str)

    parser.add_argument('-n',
                        '--number',
                        help='Number of positions to shift (default: 3)',
                        metavar='int',
                        type=int,
                        default=3)

    parser.add_argument('-d',
                        '--decode',
                        help='Decode the file (default: False)',
                        action='store_true')

    parser.add_argument(
        '-o',
        '--outfile',
        help='Output file to write the result (default: std.out)',
        metavar='FILE',
        type=str,
        default=None)

    args = parser.parse_args()

    # Check that the file exists
    if not os.path.isfile(args.file):
        parser.error(
            f"can't open '{args.file}': [Errno 2] No such file or directory: '{args.file}'"
        )

    return args


# --------------------------------------------------
def process_file(args):
    """Process the input file and apply Caesar Cipher"""

    # Open the input file for reading
    with open(args.file, "r") as infile:
        lines = infile.readlines()

    # Process each line with the Caesar shift
    shifted_lines = []
    for line in lines:
        shifted_line = ''.join(
            shift_letter(char, args.number, args.decode) for char in line)
        shifted_lines.append(shifted_line)

    # Output result to either a file or standard output
    if args.outfile:
        with open(args.outfile, "w") as outfile:
            outfile.writelines(shifted_lines)
    else:
        for line in shifted_lines:
            print(line, end='')


# --------------------------------------------------
def main():
    args = get_args()
    process_file(args)


# --------------------------------------------------
if __name__ == '__main__':
    main()
