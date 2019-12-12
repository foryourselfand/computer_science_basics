from sys import argv

from args_getter import ArgsGetter
from code_to_word_translator import CodeToWordTranslator


def main():
    args_getter = ArgsGetter()
    codes = args_getter.get_codes(argv)

    code_to_word_translator = CodeToWordTranslator()
    words = code_to_word_translator.translate_codes_to_words(codes)
    for code, word in zip(codes, words):
        print('{:>4s}: {}'.format(code, word))


if __name__ == '__main__':
    main()
