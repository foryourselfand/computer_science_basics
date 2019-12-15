from abc import abstractmethod
from typing import List


class Formatter:
    def _get_header(self) -> List[str]:
        pass
    
    @abstractmethod
    def format_output(self, inputs: List[List[str]], name: str = ''):
        pass
