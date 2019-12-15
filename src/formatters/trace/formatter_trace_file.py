from typing import List

from src.formatters.trace.formatter_trace import FormatterTrase
from src.utils.helper import Helper


class FormatterTraseFile(FormatterTrase):
    def format_output(self, inputs: List[List[str]], name: str = ''):
        with open(f'{Helper.get_project_root()}/tracing/{name}.txt', 'w+') as file_output:
            print(self._get_header(), file = file_output)
            for line in inputs:
                print('{:3s} {:4s} {:3s} {:4s} {:3s} {:4s} {:3s} {:3s} {:4s} {:4s} {:3s} {:4s}'.format(*line),
                      file = file_output)
