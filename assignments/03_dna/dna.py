#!/usr/bin/env python3
"""
Author : Xavier Griggs
Date   : 2025-02-16
Purpose: sequencing dna
"""
import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Tetranucleotide frequency',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('DNA',
                        metavar='DNA',
                        help='Input DNA sequence')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Count tetranucleotide frequency"""

    args = get_args()
    dna = args.DNA.upper()
    counts = {base: dna.count(base) for base in 'ACGT'}

    print(counts['A'], counts['C'], counts['G'], counts['T'])


# --------------------------------------------------
if __name__ == '__main__':
    main()
