import time
from collections import namedtuple
from pprint import pprint
from typing import Dict, List

from src.bgcomp_reader.bcomp_reader import BCompReader
from src.bgcomp_reader.screen_config import ScreenConfig
from src.variant_getter import VariantGetter
from src.words.words_writer import WordsWriter
import pickle
from src.utils.helper import get_project_root


def from_bin_to_hex(input_number: str, zeroes_count: int):
    return hex(int(input_number, 2))[2:].zfill(zeroes_count).upper()


def main():
    file_name = 'variants/1274.txt'

    variant_getter = VariantGetter()
    variant_getter.read_program(file_name)
    program = variant_getter.program

    words_writer = WordsWriter()
    words_writer.write_program(program, variant_getter.program_start)

    bcomp_reader = BCompReader()

    ram_all: Dict[str, str] = dict()
    result: List[List[str]] = list()

    wait_flag = True
    for address, data in variant_getter.program.items():
        if wait_flag:
            if variant_getter.program_start == data.address_bin:
                wait_flag = False
        if wait_flag:
            continue
        if not data.is_command:
            continue

        print(address, data.data_hex)
        flags, ram_current = bcomp_reader.get_flags_and_ram()

        pprint(flags)
        pprint(ram_current)
        print('-' * 50)

        ip = from_bin_to_hex(flags['IP'], 3)
        cr = from_bin_to_hex(flags['CR'], 4)
        ar = from_bin_to_hex(flags['AR'], 3)
        dr = from_bin_to_hex(flags['DR'], 4)
        sp = from_bin_to_hex(flags['SP'], 3)
        br = from_bin_to_hex(flags['BR'], 4)
        ac = from_bin_to_hex(flags['AC'], 4)
        nzvc = flags['PS'][-4:]
        print('nzvc:', nzvc)

        output_new_address, output_new_code = '', ''
        for key_current, value_current in ram_current.items():
            if key_current not in ram_all.keys():
                ram_all[key_current] = value_current
            value_all = ram_all[key_current]
            if value_current != value_all:
                print(f'address: {key_current};\tnew_code: {value_current}')
                ram_all[key_current] = value_current
                output_new_address, output_new_code = key_current, value_current
        print('output_new_address:', output_new_address)
        print('output_new_code:', output_new_code)

        temp_output = [address, data.data_hex,
                       ip, cr, ar, dr, sp, br, ac, nzvc,
                       output_new_address, output_new_code]
        result.append(temp_output)

        time.sleep(2.5)
        words_writer.press_continue()
        time.sleep(2.5)

    for output in result:
        print(output)

    with open(f'{get_project_root()}/output.pickle', 'wb') as output_file:
        pickle.dump(result, output_file)


if __name__ == '__main__':
    main()
