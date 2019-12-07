#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility"""

__author__ = "SmileySlays"


import sys
import argparse


def create_parser():
    parser = argparse.ArgumentParser(
        description='Perform transformation on input text.')
    parser.add_argument("text", help="text to be manipulated")
    parser.add_argument('-u', "--upper", action="store_true",
                        help='convert text to uppercase')
    parser.add_argument('-l', "--lower",
                        help='convert text to lowercase', action="store_true")
    parser.add_argument('-t', "--title",
                        help='convert text to titlecase', action="store_true")
    return parser


def main(args):
    """Implementation of echo"""
    parser = create_parser()
    args = parser.parse_args(args)

    if not args:
        parser.print_usage()
        sys.exit(1)

    text = args.text

    if args.upper:
        text = text.upper()
    elif args.lower:
        text = text.lower()
    elif args.title:
        text = text.title()

    return text


if __name__ == '__main__':
    print(main(sys.argv[1:]))
