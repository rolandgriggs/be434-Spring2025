#!/usr/bin/env python3
"""
Author : Xavier Griggs
Date   : 2025-04-30
Purpose: Transcribe DNA sequences into RNA and save to output file"""

import argparse
import os
import sys


# --------------------------------------------------
def transcribe_dna_to_rna(dna_sequence):
    """Transcribe a DNA sequence into RNA by replacing T with U"""
    return dna_sequence.replace('T', 'U')


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Transcribe DNA into RNA',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # Argument for input DNA file
    parser.add_argument('files',
                        metavar='FILE',
                        nargs='+',
                        help='One or more input DNA files')

    #default = "out"
    parser.add_argument('-o',
                        '--out_dir',
                        help='Output directory for RNA files (default: out)',
                        metavar='DIR',
                        type=str,
                        default='out')

    return parser.parse_args()


# --------------------------------------------------
def process_files(args):
    """Process the input files, transcribe DNA to RNA, and write to output dir"""

    # Make sure the output dir exists
    if not os.path.exists(args.out_dir):
        os.makedirs(args.out_dir)

    total_sequences = 0
    for input_file in args.files:
        # Check if the file exists
        if not os.path.isfile(input_file):
            # Only print the usage message (not error message)
            print(f"Usage: {sys.argv[0]} [-h] [-o DIR] FILE [FILE ...]")
            print(f"No such file or directory: '{input_file}'")
            sys.exit(1)  # Exit with a non-zero code if file is missing

        # Read the file and process
        with open(input_file, 'r') as infile:
            lines = infile.readlines()

        # Create an output file
        output_file_path = os.path.join(args.out_dir,
                                        os.path.basename(input_file))

        with open(output_file_path, 'w') as outfile:
            for line in lines:
                dna_sequence = line.strip()
                if dna_sequence:  # Only transcribe non-empty lines
                    rna_sequence = transcribe_dna_to_rna(dna_sequence)
                    outfile.write(rna_sequence + '\n')
                    total_sequences += 1
    print(
        f'Done, wrote {total_sequences} sequence{"s" if total_sequences > 1 else ""} in {len(args.files)} file{"s" if len(args.files) > 1 else ""} to directory "{args.out_dir}".'
    )


# --------------------------------------------------
def main():
    args = get_args()
    process_files(args)


# --------------------------------------------------
if __name__ == '__main__':
    main()
