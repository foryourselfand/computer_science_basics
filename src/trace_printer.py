import pickle
from typing import List

from src.formatters.formatter import Formatter
from src.formatters.trace.formatter_trace_csv import FormatterTraceCSV
from src.formatters.trace.formatter_trace_txt import FormatterTraceTxt
from src.formatters.trace.formatter_trace_print import FormatterTracePrint
from src.utils.args_getter import ArgsGetter
from src.utils.helper import Helper


class TracePrinter:
    @staticmethod
    def print_trace(file_name_short: str, debug_print: bool = True):
        with open(f'{Helper().get_project_root()}/pickles/{file_name_short}.pickle', 'rb') as output_file:
            trace_output = pickle.load(output_file)
        
        formatters: List[Formatter] = [FormatterTraceTxt(), FormatterTraceCSV()]
        
        if debug_print:
            formatters.append(FormatterTracePrint())
        
        for formatter in formatters:
            formatter.format_outputs(trace_output, file_name_short)


def main():
    file_name_short, file_name_full = ArgsGetter.get_short_full_file_name('printing output trace from pickle folder')
    
    TracePrinter.print_trace(file_name_short)


if __name__ == '__main__':
    main()
