import argparse
from typing import Tuple

from src.utils.helper import Helper


class ArgsGetter:
    @staticmethod
    def get_short_full_file_name(description: str) -> Tuple[str, str]:
        parser = argparse.ArgumentParser(description = description)
        parser.add_argument('file_name', help = 'variants/{file_name}.txt', type = str)
        parser.add_argument('--raw', '-r', help = 'not from folder variants', action = 'store_true')
        
        args = parser.parse_args()
        
        file_name_short = args.file_name
        base_file_dir = f'{Helper.get_project_root()}'
        if args.raw:
            file_name_full = f'{base_file_dir}/{file_name_short}.txt'
        else:
            file_name_full = f'{base_file_dir}/variants/{file_name_short}.txt'
        
        return args.file_name, file_name_full


def main():
    file_name_short, file_name_full = ArgsGetter.get_short_full_file_name('test description')
    print('file_name_short:', file_name_short)
    print('file_name_full:', file_name_full)


if __name__ == '__main__':
    main()
