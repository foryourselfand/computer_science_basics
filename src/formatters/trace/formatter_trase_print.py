from typing import List
from src.formatters.formatter import Formatter
from src.formatters.trace.formatter_trace import FormatterTrase


class FormatterTrasePrint(FormatterTrase):
    def format_output(self, inputs: List[List[str]], name: str = ''):
        print(self._get_header())
        for line in inputs:
            print('{:3s} {:4s} {:3s} {:4s} {:3s} {:4s} {:3s} {:3s} {:4s} {:4s} {:3s} {:4s}'.format(*line))
