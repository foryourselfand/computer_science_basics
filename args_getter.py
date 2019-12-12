from typing import List
from src.utils.helper import *


class ArgsGetter:
    def get_codes(self, argv: List[str]) -> List[str]:
        assert len(argv) >= 2
        args = argv[1:]

        if len(args) == 1:
            arg = args[0]
            if arg.endswith('.txt'):
                return self.__get_codes_from_file(arg)
        return args

    def __get_codes_from_file(self, file_name: str):
        with open(f'{get_project_root()}/variants/{file_name}', 'r') as file_input:
            return file_input.read().splitlines()
