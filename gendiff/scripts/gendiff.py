#!/usr/bin/env python3
import argparse
import json


def get_str(val):
    if val is False:
        return 'false'
    elif val is True:
        return 'true'
    else:
        return val


def generate_diff(file_1, file_2):
    str_1 = json.load(open(f'{file_1}'))
    str_2 = json.load(open(f'{file_2}'))

    dict_1 = json.loads(json.dumps(str_1, sort_keys=True))
    dict_2 = json.loads(json.dumps(str_2, sort_keys=True))

    output = '{'
    for res in dict_1:
        if res in dict_2:
            res_1 = get_str(dict_1[res])
            res_2 = get_str(dict_2[res])
            if res_1 == res_2:
                output = f'{output}\n    {res}: {res_1}'
            else:
                output = f'{output}\n  - {res}: {res_1}'
                output = f'{output}\n  + {res}: {res_2}'
            del dict_2[res]
        else:
            output = f'{output}\n  - {res}: {get_str(dict_1[res])}'

    for res in dict_2:
        output = f'{output}\n  + {res}: {get_str(dict_2[res])}'

    output = f'{output}' + '\n}'
    return output


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
