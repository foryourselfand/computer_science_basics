import pickle
import time
from typing import Dict, List

from src.bgcomp_reader.bcomp_reader import BCompReader
from src.formatters.formatter import Formatter
from src.formatters.trace.formatter_trace_print import FormatterTracePrint
from src.program_getter import ProgramGetter
from src.trace_printer import TracePrinter
from src.utils.args_getter import ArgsGetter
from src.utils.helper import Helper
from src.words_writer import WordsWriter


class TraceGetter:
    def __init__(self, time_to_sleep: float = 2.5):
        self.time_to_sleep = time_to_sleep
        
        self.variant_getter = ProgramGetter()
        self.words_writer = WordsWriter()
        self.bcomp_reader = BCompReader()
        
        self.ram_all: Dict[str, str] = dict()
        self.result: List[List[str]] = list()
        
        self.formatter: Formatter = FormatterTracePrint()
    
    def get_trace(self, full_file_name: str):
        self.ram_all.clear()
        self.result.clear()
        
        self.variant_getter.read_program(full_file_name)
        program = self.variant_getter.program
        program_start = self.variant_getter.program_start
        
        self.words_writer.write_program(program, program_start)
        
        wait_flag = True
        for address, data in program.items():
            if wait_flag:
                if program_start == data.address_bin:
                    wait_flag = False
                    self.formatter.format_output_header()
            if wait_flag:
                continue
            if not data.is_command:
                continue
            
            time.sleep(self.time_to_sleep)
            self.words_writer.press_continue()
            time.sleep(self.time_to_sleep)
            
            flags, ram_current = self.bcomp_reader.get_flags_and_ram()
            
            ip = Helper.from_bin_to_hex(flags['IP'], 3)
            cr = Helper.from_bin_to_hex(flags['CR'], 4)
            ar = Helper.from_bin_to_hex(flags['AR'], 3)
            dr = Helper.from_bin_to_hex(flags['DR'], 4)
            sp = Helper.from_bin_to_hex(flags['SP'], 3)
            br = Helper.from_bin_to_hex(flags['BR'], 4)
            ac = Helper.from_bin_to_hex(flags['AC'], 4)
            nzvc = flags['PS'][-4:]
            
            output_new_address, output_new_code = self.get_new_address_and_new_code(ram_current)
            
            temp_output = [address, data.data_hex,
                           ip, cr, ar, dr, sp, br, ac, nzvc,
                           output_new_address, output_new_code]
            self.formatter.format_output(temp_output)
            self.result.append(temp_output)
        return self.result
    
    def get_new_address_and_new_code(self, ram_current):
        output_new_address, output_new_code = '   ', '    '
        for key_current, value_current in ram_current.items():
            if key_current not in self.ram_all.keys():
                self.ram_all[key_current] = value_current
            value_all = self.ram_all[key_current]
            if value_current != value_all:
                self.ram_all[key_current] = value_current
                output_new_address, output_new_code = key_current, value_current
        return output_new_address, output_new_code


def main():
    file_name_short, file_name_full = ArgsGetter.get_short_full_file_name('typing you variant and printing trace')
    
    tracer = TraceGetter(1)
    result = tracer.get_trace(file_name_full)
    
    with open(f'{Helper().get_project_root()}/pickles/{file_name_short}.pickle', 'wb+') as output_file:
        pickle.dump(result, output_file)
        
    TracePrinter.print_trace(file_name_short, False)


if __name__ == '__main__':
    main()
