import pyautogui
from src.variant_getter import VariantGetter
from src.utils.helper import ProgramType


class WordsWriter:
    def write_program(self, program: ProgramType, program_start: str):
        self.__switch_to_next_window()

        address_last = 0
        for address_new, data in program.items():

            address_current = data.address_int
            address_delta = address_current - address_last

            if address_delta != 1:
                self.__write_address(data.address_bin)

            self.__write_command(data.data_bin)

            address_last = address_current

        self.__write_address(program_start)

    @staticmethod
    def __switch_to_next_window():
        pyautogui.keyDown('command')
        pyautogui.keyDown('tab')

        pyautogui.keyUp('command')
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
    file_name = 'variants/4114.txt'

    variant_getter = VariantGetter()
    variant_getter.read_program(file_name)
    program = variant_getter.program

    words_writer = WordsWriter()
    words_writer.write_program(program, variant_getter.program_start)


if __name__ == '__main__':
    main()
