from sys import argv

import pyautogui

from args_getter import ArgsGetter
from code_to_word_translator import CodeToWordTranslator


def main():
    codes = ArgsGetter().get_codes(argv)

    code_to_word_translator = CodeToWordTranslator()
    words = code_to_word_translator.translate_codes_to_words(codes)

    pyautogui.hotkey('command', 'tab')
    pyautogui.hotkey('command', 'tab')
    for code, word in zip(codes, words):
        for word_elem in word:
            if word_elem == ' ':
                continue
            pyautogui.typewrite(word_elem)
        if len(code) == 3:  # enter address
            pyautogui.press('f4')
        elif len(code) == 4:  # write
            pyautogui.press('f5')


if __name__ == '__main__':
    main()
