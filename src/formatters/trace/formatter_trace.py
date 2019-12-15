from abc import ABC
from typing import List

from src.formatters.formatter import Formatter


class FormatterTrace(Formatter, ABC):
    def __init__(self):
        self._line_formatted = '{:>7s} {:>8s} {:>4s} {:>5s} {:>4s} {:>5s} {:>4s} {:>5s} {:>5s} {:>5s} {:>12s} {:>10s}'
    
    def _get_header(self) -> List[str]:
        return ['Адресс', 'Код', 'IP', 'CR', 'AR', 'DR', 'SP', 'BR', 'AC', 'NZVC', 'Новый адрес', 'Новый Код']
