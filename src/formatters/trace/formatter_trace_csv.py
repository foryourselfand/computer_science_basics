import csv
from typing import List

from src.formatters.trace.formatter_trace import FormatterTrace
from src.utils.helper import Helper


class FormatterTraceCSV(FormatterTrace):
    def __init__(self):
        super().__init__()
        self.csv_writer = None
    
    def format_output(self, input_element: List[str]):
        self.csv_writer.writerow(input_element)
    
    def format_outputs(self, input_elements: List[List[str]], name: str = ''):
        with open(f'{Helper.get_project_root()}/tracing/csv/{name}.csv', 'w+') as file_temp:
            self.csv_writer = csv.writer(file_temp)
            self.format_output_header()
            for line in input_elements:
                self.format_output(line)
