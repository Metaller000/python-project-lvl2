import pytest
import os
from gendiff.scripts.generate_diff import generate_diff

full_path = f'{os.path.dirname(os.path.abspath(__file__))}/fixtures'


def test_json_generate_diff_1():
    data_1 = ''
    with open(f'{full_path}/result_1') as file:
        data_1 = file.read()

    data_2 = generate_diff(f'{full_path}/file_1.json',
                           f'{full_path}/file_2.json')

    assert data_2 == data_1


def test_json_generate_diff_2():
    data_1 = ''
    with open(f'{full_path}/result_2') as file:
        data_1 = file.read()

    data_2 = generate_diff(f'{full_path}/file_3.json',
                           f'{full_path}/file_4.json')
    assert data_2 == data_1


def test_yaml_generate_diff_1():
    data_1 = ''
    with open(f'{full_path}/result_1') as file:
        data_1 = file.read()

    data_2 = generate_diff(f'{full_path}/file_1.yml',
                           f'{full_path}/file_2.yml')
    assert data_2 == data_1


def test_yaml_generate_diff_2():
    data_1 = ''
    with open(f'{full_path}/result_2') as file:
        data_1 = file.read()

    data_2 = generate_diff(f'{full_path}/file_3.yml',
                           f'{full_path}/file_4.yml')
    assert data_2 == data_1


def test_json_yaml_generate_diff_1():
    data_1 = ''
    with open(f'{full_path}/result_1') as file:
        data_1 = file.read()

    data_2 = generate_diff(f'{full_path}/file_1.json',
                           f'{full_path}/file_2.yml')
    assert data_2 == data_1


def test_json_yaml_generate_diff_2():
    data_1 = ''
    with open(f'{full_path}/result_2') as file:
        data_1 = file.read()

    data_2 = generate_diff(f'{full_path}/file_3.json',
                           f'{full_path}/file_4.yml')
    assert data_2 == data_1


def test_json_generate_diff_plain_1():
    data_1 = ''
    with open(f'{full_path}/result_3') as file:
        data_1 = file.read()

    stile = 'plain'
    data_2 = generate_diff(f'{full_path}/file_3.json',
                           f'{full_path}/file_4.json',
                           stile)
    assert data_2 == data_1


def test_yaml_generate_diff_plain_1():
    data_1 = ''
    with open(f'{full_path}/result_3') as file:
        data_1 = file.read()

    stile = 'plain'
    data_2 = generate_diff(f'{full_path}/file_3.yml',
                           f'{full_path}/file_4.yml',
                           stile)
    assert data_2 == data_1


def test_json_yaml_generate_diff_plain_1():
    data_1 = ''
    with open(f'{full_path}/result_3') as file:
        data_1 = file.read()

    stile = 'plain'
    data_2 = generate_diff(f'{full_path}/file_3.json',
                           f'{full_path}/file_4.yml',
                           stile)
    assert data_2 == data_1
