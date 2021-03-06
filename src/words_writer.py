import os

import pyautogui

from src.program_getter import ProgramGetter
from src.utils.args_getter import ArgsGetter
from src.utils.helper import Helper


class WordsWriter:
    def __init__(self):
        self.key: str = ''
        if os.sys.platform == 'win32':
            self.key = 'alt'
        elif os.sys.platform == 'darwin':
            self.key = 'command'

    def write_program(self, program: Helper.ProgramType, program_start: str):
        self.switch_to_next_window()

        address_last = 0
        for address_new, data in program.items():

            address_current = data.address_int
            address_delta = address_current - address_last

            if address_delta != 1:
                self.__write_address(data.address_bin)

            self.__write_command(data.data_bin)

            address_last = address_current

        self.__write_address(program_start)

    def switch_to_next_window(self):
        pyautogui.keyDown(self.key)
        pyautogui.keyDown('tab')

        pyautogui.keyUp(self.key)
        pyautogui.keyUp('tab')

    @staticmethod
    def __write_command(command: str):
        pyautogui.typewrite(command)
        pyautogui.press('f5')

    @staticmethod
    def __write_address(address: str):
        pyautogui.typewrite(address)
        pyautogui.press('f4')

    @staticmethod
    def press_continue():
        pyautogui.press('f8')


def main():
    file_name_short, file_name_full = ArgsGetter.get_short_full_file_name('switching to bcomp and typing yours variant')

    variant_getter = ProgramGetter()
    variant_getter.read_program(file_name_full)
    program = variant_getter.program

    words_writer = WordsWriter()
    words_writer.write_program(program, variant_getter.program_start)


if __name__ == '__main__':
    main()
