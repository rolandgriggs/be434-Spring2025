#!/usr/bin/env python3
"""
Author : Xavier Griggs
Date   : 2025-03-02
Purpose: Add Your Purpose
"""

import argparse
import os
# --------------------------------------------------
def get_args():
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Print the reverse complement of DNA',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('DNA',
                        metavar='DNA',
                        help='Input sequence or file')

    return parser.parse_args()

def reverse_complement(dna):
    """Return the reverse complement of a DNA sequence"""
    # only problem is the maketrans doesn't account for the case of the character
    
    complement = str.maketrans('ACGTacgt', 'TGCAtgca')
    return dna.translate(complement)[::-1]

# --------------------------------------------------
def main():
    """Main execution"""
    args = get_args()

    # Construct file path in 'inputs/' directory
    #file_path = os.path.join('inputs', args.DNA)
    # the user is expected to provide the file path on the command line
    file_path = args.DNA

    # Try reading as a file; if fails, treat as sequence
    if os.path.isfile(file_path):
        with open(file_path, 'rt') as fh:
            dna_seq = fh.read().strip()
    else:
        dna_seq = args.DNA.strip()

    # Print reverse complement
    print(reverse_complement(dna_seq))


# --------------------------------------------------
if __name__ == '__main__':
    main()
