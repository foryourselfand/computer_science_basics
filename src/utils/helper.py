from pathlib import Path
from typing import List, Type, Union, Tuple, Dict
from collections import namedtuple

DataType = namedtuple('DataType', ['data', 'is_command'])
ProgramType: Type = Dict[str, DataType]


def get_project_root() -> Path:
    return Path(__file__).parent.parent.parent


def get_read_file(full_file_name: str, encoding: str = 'utf-8') -> List[str]:
    with open(full_file_name, 'r', encoding = encoding) as file_input:
        return file_input.read().splitlines()
