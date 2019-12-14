from pathlib import Path
from typing import List, Type, Union, Tuple, Dict
from collections import namedtuple

DataType = namedtuple('DataType', ['data_hex', 'data_bin', 'is_command', 'address_int', 'address_bin'])
ProgramType: Type = Dict[str, DataType]
# OutputType = namedtuple('Output',
#                         ['address', 'code',
#                          'IP', 'CR', 'AR', 'DR', 'SP', 'BR', 'AC', 'NZVC',
#                          'address_changed', 'new_code'])


def get_project_root() -> Path:
    return Path(__file__).parent.parent.parent


def get_read_file(full_file_name: str, encoding: str = 'utf-8') -> List[str]:
    with open(full_file_name, 'r', encoding = encoding) as file_input:
        return file_input.read().splitlines()


def translate_code_to_word(code: str) -> str:
    word: str = bin(int(code, 16))[2:]
    word_with_zeroes = word.zfill(16)
    return word_with_zeroes
