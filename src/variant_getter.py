from pprint import pprint

from src.utils.helper import get_project_root, ProgramType, DataType


class VariantGetter:
    def __init__(self):
        self.program: ProgramType = dict()
        self.address_start: int = 0

    def get_program(self, full_file_name: str) -> ProgramType:
        address_current: int = 0

        with open(f'{get_project_root()}/{full_file_name}', 'r') as file_input:
            for line_raw in file_input.read().splitlines():
                address_flag = 'a' in line_raw
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

                if address_start_flag:
                    self.address_start = address_current
                type_flag = command_flag

                hex_key = str(hex(address_current))[2:].upper().zfill(3)
                self.program[hex_key] = DataType(line, type_flag)

                address_current += 1
        return self.program


def main():
    file_name = 'variants/4114.txt'

    variant_getter = VariantGetter()
    program = variant_getter.get_program(file_name)
    pprint(program)


if __name__ == '__main__':
    main()
