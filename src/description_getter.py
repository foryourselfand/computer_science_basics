import pickle
from pprint import pprint
from typing import Dict

from src.utils.helper import Helper


def get_commands_pickle() -> Dict:
    with open(f'{Helper.get_project_root()}/commands_dict.pickle', 'rb') as file:
        data = pickle.load(file)
    return data


def main():
    commands_pickle = get_commands_pickle()
    pprint(commands_pickle)


if __name__ == '__main__':
    main()
