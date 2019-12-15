import pickle

from src.utils.helper import Helper


def main():
    variant = 'slava'
    
    with open(f'{Helper().get_project_root()}/pickles/{variant}.pickle', 'rb') as output_file:
        result = pickle.load(output_file)
    
    # pprint(result)
    
    for output in result:
        print('{:3s} {:4s} {:3s} {:4s} {:3s} {:4s} {:3s} {:3s} {:4s} {:4s} {:3s} {:4s}'.format(*output))


if __name__ == '__main__':
    main()
