from pprint import pprint

from src.utils.helper import get_project_root
import pickle


def main():
    with open(f'{get_project_root()}/output.pickle', 'rb') as output_file:
        result = pickle.load(output_file)

    pprint(result)

    for output in result:
        print('{:3s} {:4s} {:3s} {:4s} {:3s} {:4s} {:3s} {:3s} {:4s} {:4s} {:3s} {:4s}'.format(*output))


if __name__ == '__main__':
    main()
