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
