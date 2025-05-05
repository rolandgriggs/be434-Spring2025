#!/usr/bin/env python3
"""
Author : Xavier Griggs
Date   : 2025-04-30
Purpose: Parse BLAST output and merge w/ metadata 
"""

import argparse
import pandas as pd
import sys
import os


# --------------------------------------------------
def get_args():

    parser = argparse.ArgumentParser(
        description='Annotate BLAST output',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-b',
                        '--blasthits',
                        help='BLAST -outfmt 6 file',
                        metavar='FILE',
                        required=True)

    parser.add_argument('-a',
                        '--annotations',
                        help='Annotations file',
                        metavar='FILE',
                        required=True)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='FILE',
                        default='out.csv')

    parser.add_argument('-d',
                        '--delimiter',
                        help='Output field delimiter',
                        metavar='DELIM',
                        default=',')

    parser.add_argument('-p',
                        '--pctid',
                        help='Minimum percent identity',
                        metavar='PCTID',
                        type=float,
                        default=0.0)

    return parser.parse_args()


# --------------------------------------------------
def guess_delimiter(filename):
    """Guess delimiter based on extension"""
    ext = os.path.splitext(filename)[-1].lower()
    return '\t' if ext in ['.tsv', '.tab', '.txt'] else ','


# --------------------------------------------------
def main():
    args = get_args()

    if not os.path.isfile(args.blasthits):
        sys.exit(f"No such file or directory: '{args.blasthits}'")

    if not os.path.isfile(args.annotations):
        sys.exit(f"No such file or directory: '{args.annotations}'")

    # Guess delimiters based on extension
    blast_delim = guess_delimiter(args.blasthits)
    anno_delim = guess_delimiter(args.annotations)

    try:
        blast_df = pd.read_csv(args.blasthits,
                               header=None,
                               delimiter=blast_delim)
        annotations_df = pd.read_csv(args.annotations, delimiter=anno_delim)
    except Exception as e:
        sys.exit(f"Error reading input files: {e}")

    # BLAST outfmt 6 headers
    blast_df.columns = [
        'qseqid', 'sseqid', 'pident', 'length', 'mismatch', 'gapopen',
        'qstart', 'qend', 'sstart', 'send', 'evalue', 'bitscore'
    ]

    # Rename metadata column for merge
    if 'seq_id' in annotations_df.columns and 'qseqid' not in annotations_df.columns:
        annotations_df.rename(columns={'seq_id': 'qseqid'}, inplace=True)

    # Filter on percent identity
    blast_df = blast_df[blast_df['pident'] >= args.pctid]

    merged = pd.merge(blast_df, annotations_df, on='qseqid', how='left')

    # Select required columns
    out_df = merged[['qseqid', 'pident', 'depth', 'lat_lon']]

    out_delim = args.delimiter if args.delimiter != ',' else guess_delimiter(
        args.outfile)

    out_df.to_csv(args.outfile, index=False, sep=out_delim)

    print(f'Exported {len(out_df)} to "{args.outfile}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
