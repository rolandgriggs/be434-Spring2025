#!/usr/bin/env python3
"""
Author : Your Name <your_email@example.com>
Date   : 2025-04-30
Purpose: Compress DNA sequences using Run-Length Encoding (RLE)
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Run-length encoding/data compression for DNA sequences',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='DNA sequence or file containing sequences')

    return parser.parse_args()


# --------------------------------------------------
def rle(seq):
    """Create RLE (Run-Length Encoding) for a single sequence"""

    encoded = []
    count = 1

    for i in range(1, len(seq)):
        if seq[i] == seq[i - 1]:
            count += 1
        else:
            encoded.append(f"{seq[i - 1]}{count if count > 1 else ''}")
            count = 1

    # Append the last base
    encoded.append(f"{seq[-1]}{count if count > 1 else ''}")

    return ''.join(encoded)


# --------------------------------------------------
def main():
    """Main function to execute the program"""

    # Get arguments from the user
    args = get_args()

    # If the input is a file, read it
    if args.text.endswith('.txt') or args.text.endswith('.fa') or args.text.endswith('.fasta'):
        with open(args.text, 'r') as f:
            for line in f:
                seq = line.strip()
                if seq:
                    print(rle(seq))
    else:
        # If the input is a single sequence, apply RLE
        seq = args.text.strip()
        print(rle(seq))


# --------------------------------------------------
if __name__ == '__main__':
    main()
