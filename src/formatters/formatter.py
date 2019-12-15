from abc import abstractmethod
from typing import List


class Formatter:
    @abstractmethod
    def _get_header(self) -> List[str]:
        pass
    
    @abstractmethod
    def format_output(self, input_element: List[str]):
        pass
    
    @abstractmethod
    def format_outputs(self, input_elements: List[List[str]], name: str = ''):
        first_len: int = len(input_elements[0])
        for input_elem in input_elements[1:]:
            assert len(input_elem) == first_len
        assert first_len == len(self._get_header())
    
    def format_output_header(self):
        self.format_output(self._get_header())
