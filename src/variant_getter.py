from pprint import pprint
from typing import List

from src.utils.helper import get_project_root, ProgramType, DataType, translate_code_to_word


class VariantGetter:
    def __init__(self):
        self.program: ProgramType = dict()
        self.program_start: str = '000'

    def read_program(self, full_file_name: str):
        address_current: int = 0

        with open(f'{get_project_root()}/{full_file_name}', 'r') as file_input:
            for line_raw in file_input.read().splitlines():
                if 'a' in line_raw or len(line_raw) == 3:
                    address_flag = True
                else:
                    address_flag = False

                address_start_flag = '+' in line_raw

                if 'v' in line_raw:
                    command_flag = False
                elif 'c' in line_raw:
                    command_flag = True
                else:
                    command_flag = True

                line = line_raw.replace('a', '').replace('+', '').replace('c', '').replace('v', '')

                if address_flag:
                    address_current = int(line, base = 16)
                    continue

                type_flag = command_flag

                address_hex = hex(address_current)[2:].upper().zfill(3)
                address_int = address_current
                address_bin = bin(address_int)[2:].zfill(16)

                if address_start_flag:
                    self.program_start = address_bin

                data_hex = line
                data_bin = translate_code_to_word(line)

                self.program[address_hex] = DataType(data_hex, data_bin, type_flag, address_int, address_bin)

                address_current += 1

    def get_addresses(self) -> List[str]:
        return list(self.program.keys())


def main():
    file_name = 'variants/4114.txt'

    variant_getter = VariantGetter()
    variant_getter.read_program(file_name)
    program = variant_getter.program
    pprint(program)

    addresses = variant_getter.get_addresses()
    pprint(addresses)


if __name__ == '__main__':
    main()
