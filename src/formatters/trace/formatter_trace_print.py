from typing import List

from src.formatters.trace.formatter_trace import FormatterTrace


class FormatterTracePrint(FormatterTrace):
    def format_outputs(self, input_elements: List[List[str]], name: str = ''):
        self.format_output_header()
        for line in input_elements:
            self.format_output(line)
    
    def format_output(self, input_element: List[str]):
        print(self._line_formatted.format(*input_element))
