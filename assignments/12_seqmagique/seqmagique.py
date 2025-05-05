#!/usr/bin/env python3
"""
Author : Your Name <your_email@example.com>
Date   : 2025-04-30
Purpose: Process FASTA files and display sequence statistics
"""

import argparse
from tabulate import tabulate
from Bio import SeqIO
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Process FASTA files and display sequence statistics',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('files',
                        metavar='FILE',
                        nargs='+',
                        help='FASTA input file(s)')

    parser.add_argument('-t',
                        '--tablefmt',
                        metavar='style',
                        default='plain',
                        help='Tabulate table style (default: plain)')

    return parser.parse_args()


# --------------------------------------------------
def get_seq_stats(fasta_file):
    """Get statistics from a FASTA file"""

    if not os.path.isfile(fasta_file):
        print(f"Usage: seqmagique.py [-h] [-t style] FILE [FILE ...]")
        print(f"No such file or directory: '{fasta_file}'")
        sys.exit(1)

    lengths = [len(rec.seq) for rec in SeqIO.parse(fasta_file, 'fasta')]
    if not lengths:
        return [fasta_file, 0, 0, "0.00", 0]

    num_seqs = len(lengths)
    min_len = min(lengths)
    max_len = max(lengths)
    avg_len = f"{sum(lengths) / num_seqs:.2f}"

    return [fasta_file, min_len, max_len, avg_len, num_seqs]


# --------------------------------------------------
def main():
    """Main function"""

    args = get_args()
    rows = []

    for file in args.files:
        try:
            stats = get_seq_stats(file)
            if stats:
                rows.append(stats)
        except Exception as e:
            sys.exit(f'Error processing {file}: {e}')

    print(tabulate(rows,
                   headers=['name', 'min_len', 'max_len', 'avg_len', 'num_seqs'],
                   tablefmt=args.tablefmt))


# --------------------------------------------------
if __name__ == '__main__':
    main()
