import pytest
from gendiff.scripts.gendiff import generate_diff

import os
full_path = os.path.dirname(os.path.abspath(__file__))

str_1 = ''
with open(f'{full_path}/fixtures/result_1') as file:
    str_1 = file.read()


def test_generate_diff():
    str_2 = generate_diff(f'{full_path}/fixtures/file_1.json',
                          f'{full_path}/fixtures/file_2.json')
    assert str_2 == str_1
