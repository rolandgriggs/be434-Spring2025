#!/usr/bin/env python3
"""
Author : Xavier Griggs
Date   : 2025-04-15
Purpose: Compute GC content of DNA sequences
"""
import argparse
import sys


# --------------------------------------------------
def get_args():
    "Get command-line arguments"

    parser = argparse.ArgumentParser(
        description='Compute GC content',
        formatter_class=argparse.HelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        help='Input sequence file',
                        type=argparse.FileType('rt'),
                        nargs='?',
                        default=sys.stdin)

    return parser.parse_args()


# --------------------------------------------------
def read_fasta(file):
    "Read a FASTA file and return a dict of {ID: sequence}"
    sequences = {}
    current_id = None
    for line in file:
        line = line.strip()
        if line.startswith('>'):
            current_id = line[1:]
            sequences[current_id] = ''
        elif current_id:
            sequences[current_id] += line
    return sequences


# --------------------------------------------------
def gc_content(seq):
    "Calculate GC content"
    gc_count = seq.count('G') + seq.count('C')
    return gc_count / len(seq) if seq else 0


# --------------------------------------------------
def main():
    "Compute and print ID with highest GC content"

    args = get_args()
    sequences = read_fasta(args.file)

    if not sequences:
        print('No sequences found', file=sys.stderr)
        sys.exit(1)

    max_id = None
    max_gc = -1

    for seq_id, seq in sequences.items():
        gc = gc_content(seq)
        if gc > max_gc:
            max_gc = gc
            max_id = seq_id

    print(f'{max_id} {max_gc * 100:.6f}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
