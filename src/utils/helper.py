from collections import namedtuple
from pathlib import Path
from typing import Dict, List, Type


class Helper:
    DataType = namedtuple('DataType', ['data_hex', 'data_bin', 'is_command', 'address_int', 'address_bin'])
    ProgramType: Type = Dict[str, DataType]
    
    @staticmethod
    def get_project_root() -> Path:
        return Path(__file__).parent.parent.parent
    
    @staticmethod
    def get_read_file(full_file_name: str, encoding: str = 'utf-8') -> List[str]:
        with open(full_file_name, 'r', encoding = encoding) as file_input:
            return file_input.read().splitlines()
    
    @staticmethod
    def translate_code_to_word(code: str) -> str:
        word: str = bin(int(code, 16))[2:]
        word_with_zeroes = word.zfill(16)
        return word_with_zeroes
    
    @staticmethod
    def from_bin_to_hex(input_number: str, zeroes_count: int):
        return hex(int(input_number, 2))[2:].zfill(zeroes_count).upper()
