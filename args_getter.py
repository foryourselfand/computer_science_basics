from typing import List

from src.utils import helper


class ArgsGetter:
    @staticmethod
    def get_codes(argv: List[str]) -> List[str]:
        assert len(argv) >= 2
        args = argv[1:]

        if len(args) == 1:
            arg = args[0]
            if arg.endswith('.txt'):
                return ArgsGetter.__get_codes_from_file(arg)
        return args

    @staticmethod
    def __get_codes_from_file(file_name: str):
        with open(f'{helper.get_project_root()}/variants/{file_name}', 'r') as file_input:
            return file_input.read().splitlines()
