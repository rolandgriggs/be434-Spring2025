#!/usr/bin/env python3
"""
Author : Xavier Griggs
Date   : 2025-04-30
Purpose:
"""

import argparse
import sys


def get_words(filehandle):
    """Return a set of all whitespace-separated words from the given file"""
    words = set()
    for line in filehandle:
        for word in line.split():
            words.add(word)
    return words


def main():
    parser = argparse.ArgumentParser(
        description='Find common words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('FILE1',
                        type=argparse.FileType('r'),
                        help='Input file 1')
    parser.add_argument('FILE2',
                        type=argparse.FileType('r'),
                        help='Input file 2')
    parser.add_argument('-o',
                        '--outfile',
                        metavar='FILE',
                        type=argparse.FileType('w'),
                        help='Output file',
                        default=sys.stdout)
    # Ensure help text for optional arguments uses the expected title
    for action_group in parser._action_groups:
        if action_group.title == 'options':
            action_group.title = 'optional arguments'
    args = parser.parse_args()
    # Get unique words from both files
    words1 = get_words(args.FILE1)
    args.FILE1.close()
    words2 = get_words(args.FILE2)
    args.FILE2.close()
    # Find common words and sort them
    common_words = sorted(words1 & words2)
    # Write results to the specified output (stdout by default)
    outfh = args.outfile
    for word in common_words:
        print(word, file=outfh)
    if outfh is not sys.stdout:
        outfh.close()


if __name__ == '__main__':
    main()
