
def convert_value(val):
    if val in ('false', 'true', 'null') or type(val) is int:
        return val
    else:
        return f'"{val}"'


def json_viev(data={}, spaces_num=0):
    spaces = spaces_num * ' '

    output = '{'
    for key, value in data.items():
        if key[-2:] == ':1':
            key_out = f'- {key[:-2]}'
        elif key[-2:] == ':2':
            key_out = f'+ {key[:-2]}'
        else:
            key_out = f'{key}'

        if type(value) is dict:
            values = json_viev(value, spaces_num + 4)
            output = f'{output}\n{spaces}    "{key_out}": {values},'
        else:
            output = f'{output}\n{spaces}    "{key_out}": {convert_value(value)},'
    output = f'{output[:-1]}\n{spaces}' + '}'

    return output
