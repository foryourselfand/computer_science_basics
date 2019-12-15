import pickle
from typing import List

from src.formatters.formatter import Formatter
from src.formatters.trace.formatter_trace_file import FormatterTraceFile
from src.formatters.trace.formatter_trace_print import FormatterTracePrint
from src.utils.helper import Helper


def main():
    variant = 'slava'
    
    with open(f'{Helper().get_project_root()}/pickles/{variant}.pickle', 'rb') as output_file:
        result = pickle.load(output_file)
    
    formatters: List[Formatter] = [FormatterTracePrint(), FormatterTraceFile()]
    for formatter in formatters:
        formatter.format_outputs(result, variant)


if __name__ == '__main__':
    main()
