#!/usr/bin/env python3
import json
import yaml


def data_sort(data):
    json_data = json.dumps(data, sort_keys=True)
    json_data = json_data.replace('null', '"null"')
    json_data = json_data.replace('true', '"true"')
    json_data = json_data.replace('false', '"false"')
    return json.loads(json_data)


def get_dict_from_file(file):
    data = {}
    if '.json' in file:
        with open(file) as f:
            data = json.load(f)
    if '.yml' in file:
        with open(file) as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
    return data


def diff(data_1, data_2):
    data = {}
    for res in data_1:
        if res in data_2:
            res_1 = data_1[res]
            res_2 = data_2[res]
            if type(res_1) is dict:
                if type(res_2) is not dict:
                    data.update({f'{res}:1': res_1})
                    data.update({f'{res}:2': res_2})
                else:
                    data.update({f'{res}': diff(res_1, res_2)})
            else:
                if res_1 == res_2:
                    data.update({f'{res}': res_1})
                else:
                    data.update({f'{res}:1': res_1})
                    data.update({f'{res}:2': res_2})
            del data_2[res]
        else:
            data.update({f'{res}:1': data_1[res]})

    for res in data_2:
        data.update({f'{res}:2': data_2[res]})

    return data


def stylish(data={}, spaces_num=0):
    spaces = spaces_num * ' '

    output = '{'
    for key, value in data.items():
        if key[-2:] == ':1':
            key_out = f'  - {key[:-2]}'
        elif key[-2:] == ':2':
            key_out = f'  + {key[:-2]}'
        else:
            key_out = f'    {key}'

        if type(value) is dict:
            values = stylish(value, spaces_num + 4)
            output = f'{output}\n{spaces}{key_out}: {values}'
        else:
            output = f'{output}\n{spaces}{key_out}: {value}'
    output = f'{output}\n{spaces}' + '}'

    return output


def generate_diff(file_1, file_2):
    data = diff(get_dict_from_file(file_1), get_dict_from_file(file_2))
    data = data_sort(data)

    return stylish(data)
