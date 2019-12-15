from abc import ABC
from typing import List

from src.formatters.formatter import Formatter


class FormatterTrace(Formatter, ABC):
    def __init__(self):
        self._line_formatted = '{:6s}\t{:7s}\t{:3s}\t{:4s}\t{:3s}\t{:4s}\t{:3s}\t{:4s}\t{:4s}\t{:3s}\t{:11s}\t{:9s}'
    
    def _get_header(self) -> List[str]:
        return ['Адресс', 'Код', 'IP', 'CR', 'AR', 'DR', 'SP', 'BR', 'AC', 'NZVC', 'Новый адрес', 'Новый Код']
