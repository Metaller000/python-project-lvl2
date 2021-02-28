import pytest
import os
from gendiff.scripts.generate_diff import generate_diff

full_path = f'{os.path.dirname(os.path.abspath(__file__))}/fixtures'

data_1 = ''
with open(f'{full_path}/result_1') as file:
    data_1 = file.read()


def test_json_generate_diff():
    data_2 = generate_diff(f'{full_path}/file_1.json',
                           f'{full_path}/file_2.json')
    assert data_2 == data_1


def test_yaml_generate_diff():
    data_2 = generate_diff(f'{full_path}/filepath1.yml',
                           f'{full_path}/filepath2.yml')
    assert data_2 == data_1


def test_json_yaml_generate_diff():
    data_2 = generate_diff(f'{full_path}/file_1.json',
                           f'{full_path}/filepath2.yml')
    assert data_2 == data_1
