from pprint import pprint
from typing import Dict, List

from src.utils.helper import Helper
import pickle

def main():
    commands_dict: Dict[str, Dict[str, List[str]]] = dict()
    command_types = ['addressed', 'if', 'io', 'unnadressed']

    dict_types = ['code', 'description', 'mnemonic', 'nzvc']

    for command_type in command_types:
        if command_type not in commands_dict.keys():
            commands_dict[command_type] = dict()

        for dict_type in dict_types:
            with open(f'{Helper.get_project_root()}/commands/{command_type}/{dict_type}.txt') as file:
                for line_raw in file.read().splitlines():
                    line = line_raw.strip().replace('  ', ' ')

                    if dict_type not in commands_dict[command_type].keys():
                        commands_dict[command_type][dict_type] = []
                    commands_dict[command_type][dict_type].append(line)

    with open(f'{Helper.get_project_root()}/commands_dict.pickle', 'wb+') as file:
        pickle.dump(commands_dict, file)
    pprint(commands_dict)


if __name__ == '__main__':
    main()
