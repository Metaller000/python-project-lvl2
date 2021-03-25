from gendiff.formaters.plain import plain
from gendiff.formaters.stylish import stylish
from gendiff.formaters.json import json
from gendiff.gen_loader import data_sort, get_dict_from_file


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


def viever(data={}, stile='stylish'):
    if stile.lower() == 'stylish':
        return stylish(data)
    elif stile.lower() == 'plain':
        return plain(data)[:-1]
    elif stile.lower() == 'json':
        return json(data)


def generate_diff(file_1, file_2, stile='stylish'):
    gen_1 = get_dict_from_file(file_1)
    gen_2 = get_dict_from_file(file_2)
    data = diff(gen_1, gen_2)
    data = data_sort(data)

    return viever(data, stile)
