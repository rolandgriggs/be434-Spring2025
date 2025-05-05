#!/usr/bin/env python3
"""
Author : Xavier Griggs
Date   : 2025-04-30
Purpose: Find conserved bases in aligned sequences
"""

import argparse


# --------------------------------------------------
def get_args():

    parser = argparse.ArgumentParser(
        description='Find conserved bases in aligned sequences',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        help='Input file containing aligned sequences')

    return parser.parse_args()


# --------------------------------------------------
def read_sequences(file):
    """Read sequences from a file w/ or w/o FASTA headers"""

    sequences = []

    with open(file) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('>'):
                continue
            sequences.append(line)

    return sequences


# --------------------------------------------------
def find_conserved(sequences):
    """Find conserved bases across sequences"""

    conserved_line = []

    # For each position in the sequences
    for i in range(len(sequences[0])):  # All sequences are assumed to have the same length
        # Get the base at the current position for all
        column = [seq[i] for seq in sequences]

        # Check if all bases are the same
        if len(set(column)) == 1:
            conserved_line.append('|')
        else:
            conserved_line.append('X')

    return ''.join(conserved_line)


# --------------------------------------------------
def main():

    args = get_args()
    sequences = read_sequences(args.file)

    # Check all sequences have same length
    if not all(len(seq) == len(sequences[0]) for seq in sequences):
        raise SystemExit('Error: Sequences are not the same length.')

    for seq in sequences:
        print(seq)
    print(find_conserved(sequences))


# --------------------------------------------------
if __name__ == '__main__':
    main()
