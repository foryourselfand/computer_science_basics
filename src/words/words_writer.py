import time
from sys import argv

import pyautogui

from src.variant_getter import VariantGetter


def main():
    file_name = 'variants/4114.txt'

    variant_getter = VariantGetter()
    variant_getter.read_program(file_name)
    program = variant_getter.program

    pyautogui.keyDown('command')
    pyautogui.keyDown('tab')

    pyautogui.keyUp('command')
    pyautogui.keyUp('tab')

    address_last = 0
    for address_new, data in program.items():

        address_current = data.address_int
        address_delta = address_current - address_last

        if address_delta != 1:
            pyautogui.typewrite(data.address_bin)
            pyautogui.press('f4')

        pyautogui.typewrite(data.data_bin)
        pyautogui.press('f5')

        address_last = address_current

    pyautogui.typewrite(variant_getter.program_start)
    pyautogui.press('f4')


if __name__ == '__main__':
    main()
