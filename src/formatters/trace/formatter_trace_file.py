from io import TextIOWrapper
from typing import List

from src.formatters.trace.formatter_trace import FormatterTrace
from src.utils.helper import Helper


class FormatterTraceFile(FormatterTrace):
    def __init__(self):
        super().__init__()
        self.file_output: TextIOWrapper = None
    
    def format_outputs(self, input_elements: List[List[str]], name: str = ''):
        with open(f'{Helper.get_project_root()}/tracing/txt/{name}.txt', 'w+') as file_temp:
            self.file_output = file_temp
            self.format_output_header()
            for line in input_elements:
                self.format_output(line)
    
    def format_output(self, input_element: List[str]):
        print(self._line_formatted.format(*input_element), file = self.file_output)
