#!/usr/bin/env python3
"""
Author :Xavier Griggs
Date   : 2025-03-14
Purpose: Add Your Purpose
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    parser = argparse.ArgumentParser(
        description='Print the reverse complement of DNA',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('dna',
                        metavar='DNA',
                        type=str,
                        help='Input sequence or file')

    args = parser.parse_args()

    if os.path.isfile(args.dna):
        args.dna = open(args.dna).read().rstrip()

    return args


# --------------------------------------------------
def reverse_complement(dna):
    complement = str.maketrans('ACGTacgt', 'TGCAtgca')
    return dna.translate(complement)[::-1]


# --------------------------------------------------
def main():
    args = get_args()
    dna = args.dna

    print(reverse_complement(dna))


# --------------------------------------------------
if __name__ == '__main__':
    main()
