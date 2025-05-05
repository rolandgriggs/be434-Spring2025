#!/usr/bin/env python3
"""
Author : Xavier Griggs
Date   : 2025-04-30
Purpose:
"""

import argparse
import random
import sys

# --------------------------------------------------
def create_pool(pctgc, max_len, seq_type):
    """ Create the pool of bases based on GC content and sequence type """

    t_or_u = 'T' if seq_type == 'dna' else 'U'
    num_gc = int((pctgc / 2) * max_len)
    num_at = int(((1 - pctgc) / 2) * max_len)

    pool = 'A' * num_at + 'C' * num_gc + 'G' * num_gc + t_or_u * num_at

    for _ in range(max_len - len(pool)):
        pool += random.choice(pool)

    return ''.join(sorted(pool))


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Create synthetic DNA or RNA sequences',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-o', '--outfile',
                        help='Output filename (default: out.fa)',
                        metavar='str',
                        type=str,
                        default='out.fa')

    parser.add_argument('-t', '--seqtype',
                        help='DNA or RNA (default: dna)',
                        metavar='str',
                        type=str,
                        choices=['dna', 'rna'],
                        default='dna')

    parser.add_argument('-n', '--numseqs',
                        help='Number of sequences to create (default: 10)',
                        metavar='int',
                        type=int,
                        default=10)

    parser.add_argument('-m', '--minlen',
                        help='Minimum length (default: 50)',
                        metavar='int',
                        type=int,
                        default=50)

    parser.add_argument('-x', '--maxlen',
                        help='Maximum length (default: 75)',
                        metavar='int',
                        type=int,
                        default=75)

    parser.add_argument('-p', '--pctgc',
                        help='Percent GC (default: 0.5)',
                        metavar='float',
                        type=float,
                        default=0.5)

    parser.add_argument('-s', '--seed',
                        help='Random seed (default: None)',
                        metavar='int',
                        type=int,
                        default=None)

    return parser.parse_args()


# --------------------------------------------------
def main():


    args = get_args()

    # Verify that pctgc is between 0 and 1
    if not 0 < args.pctgc < 1:
        print(f"Usage: {sys.argv[0]} [-h] [-o DIR] FILE [FILE ...]", end=' ')
        print(f'--pctgc "{args.pctgc}" must be between 0 and 1', end=' ')
        sys.exit(1)

    # Set random seed
    random.seed(args.seed)

    # Create the base pool
    pool = create_pool(args.pctgc, args.maxlen, args.seqtype)

    # Open output file 
    with open(args.outfile, 'w') as outfile:
        for i in range(args.numseqs):
            seq_len = random.randint(args.minlen, args.maxlen)
            seq = ''.join(random.sample(pool, seq_len))

            # Write to FASTA
            outfile.write(f'>{i+1}\n')
            outfile.write(f'{seq}\n')

    print(f'Done, wrote {args.numseqs} {args.seqtype.upper()} sequences to "{args.outfile}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
