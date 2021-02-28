#!/usr/bin/env python3
import json
import yaml


def get_str(val):
    if val is False:
        return 'false'
    elif val is True:
        return 'true'
    elif val is None:
        return 'null'
    else:
        return val


def get_dict_from_file(file):
    data = {}
    if '.json' in file:
        with open(file) as f:
            data = json.load(f)
            data = json.loads(json.dumps(data, sort_keys=True))
    if '.yml' in file:
        with open(file) as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            data = yaml.load(yaml.dump(data), Loader=yaml.FullLoader)
    return data


def generate_diff(file_1, file_2):
    dict_1 = get_dict_from_file(file_1)
    dict_2 = get_dict_from_file(file_2)

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
