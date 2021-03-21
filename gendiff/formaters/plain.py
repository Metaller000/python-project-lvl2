def complex_or_val(value):
    ret_val = ""
    if type(value) is not dict:
        if value not in ['false', 'true', 'null']:
            ret_val = f"'{value}'"
        else:
            ret_val = value
    else:
        ret_val = '[complex value]'
    return ret_val


def plain(data={}, parent=''):
    f_str = 'Property'
    rem_str = 'was removed'
    upd_str = 'was updated. From'
    add_str = 'was added with value:'
    output = ''
    prev_key = ''
    for key, value in data.items():
        if key[-2:] == ':1':
            key_out = f'{key[:-2]}'
            prev_key = key_out
            if parent == '':
                parent = key_out
            else:
                parent = f'{parent}.{key_out}'
                parent = parent.replace('..', '.')

            value_plus = data.get(f'{key[:-2]}:2')
            if value_plus is not None:
                trans = f'{upd_str} {complex_or_val(value)}'
                trans = f'{trans} to {complex_or_val(value_plus)}'
                output = f"{output}{f_str} '{parent}' {trans}\n"
            else:
                output = f"{output}{f_str} '{parent}' {rem_str}\n"

        elif key[-2:] == ':2':
            if prev_key == key[:-2]:
                continue

            key_out = f'{key[:-2]}'
            if parent == '':
                parent = key_out
            else:
                parent = f'{parent}.{key_out}'
                parent = parent.replace('..', '.')
            output = f"{output}{f_str} '{parent}' "
            output = f"{output}{add_str} {complex_or_val(value)}\n"

        elif type(data.get(key)) is dict:
            key_out = f'{key}'
            if parent == '':
                parent = key_out
            else:
                parent = f'{parent}.{key_out}'
                parent = parent.replace('..', '.')

            output = output + plain(value, parent)

        parent = parent.replace(f'{key_out}', '')

    return output
