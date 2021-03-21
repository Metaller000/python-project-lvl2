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
