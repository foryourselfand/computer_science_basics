from abc import ABC
from typing import List

from src.formatters.formatter import Formatter


class FormatterTrase(Formatter, ABC):
    def _get_header(self) -> List[str]:
        return ['Адресс', 'Код', 'IP', 'CR', 'AR', 'DR', 'SP', 'BR', 'AC', 'NZVC', 'Новый адрес', 'Новый Код']
