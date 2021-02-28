#!/usr/bin/env python3
import argparse
from gendiff.scripts.generate_diff import generate_diff


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)

    parser.add_argument('-f', '--format', dest='FORMAT',
                        help='set format of output')

    args = parser.parse_args()
    if args.first_file is not None and args.second_file is not None:
        print(generate_diff(args.first_file, args.second_file))
    else:
        print(args.accumulate(args.integers))


if __name__ == '__main__':
    main()
