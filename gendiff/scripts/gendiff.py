#!/usr/bin/env python3
import argparse
from gendiff.generate_diff import generate_diff


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)

    parser.add_argument('-f', '--format', dest='FORMAT', type=str,
                        help='set format of output')

    args = parser.parse_args()
    if args.first_file is not None and args.second_file is not None:
        if args.FORMAT is None:
            print(generate_diff(args.first_file, args.second_file))
        else:
            print(generate_diff(args.first_file, args.second_file, args.FORMAT))
    else:
        print(args.accumulate(args.integers))


if __name__ == '__main__':
    main()
