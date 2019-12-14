from typing import Dict, Tuple, List

from PIL.Image import Image
from pytesseract import pytesseract

from src.size import Size
from src.utils.hash_list import HashList


class BCompReader:
    def __init__(self):
        self.__flags: Dict[str, str] = dict()
        self.__ram: Dict[str, str] = dict()
        self.__delay_y: int = 84

    def get_flags_and_ram(self, flags_config: Dict[HashList, Size], ram_size: Size, screenshot: Image) \
            -> Tuple[Dict[str, str], Dict[str, str]]:
        self.process_computer(flags_config, ram_size, screenshot)
        return self.get_flags(), self.get_ram()

    def process_computer(self, flags_config: Dict[HashList, Size], ram_size: Size, screenshot: Image):
        self.__flags = dict()
        self.__ram = dict()

        self.__process_flags(flags_config, screenshot)
        self.__process_ram(ram_size, screenshot)

    def get_flags(self):
        return self.__flags

    def get_ram(self):
        return self.__ram

    def __process_flags(self, flags_config: Dict[HashList, Size], screenshot: Image):
        for names, size in flags_config.items():
            for y_multiplier, name_key in enumerate(names):
                text_temp = self.__read_flag(size, screenshot)
                self.__flags[name_key] = text_temp

    def __process_ram(self, ram_size: Size, screenshot: Image):
        ram_image = screenshot.crop((ram_size.x, ram_size.y,
                                     ram_size.x + ram_size.width, ram_size.y + ram_size.height))
        allowed_digits = '0123456789'
        allowed_chars_lower = 'abcdef'
        allowed_chars_upper = 'ABCDEF'
        allowed_chars = allowed_digits + allowed_chars_lower + allowed_chars_upper
        config_temp = f'tessedit_char_whitelist={allowed_chars}'

        ram_str = pytesseract.image_to_string(ram_image, lang = 'eng', config = config_temp)
        ram_list = self.__get_ram_list(ram_str)
        self.__fill_ram_dict(ram_list)

    def __read_flag(self, size: Size, screenshot: Image) -> str:
        screenshot_part: Image = screenshot.crop((size.x, size.y,
                                                  size.x + size.width, size.y + size.height))
        text: str = pytesseract.image_to_string(screenshot_part)
        return text

    def __fill_ram_dict(self, ram_list: List[str]):
        len_half = len(ram_list) // 2
        for elem_key, elem_value in zip(ram_list[:len_half], ram_list[len_half:]):
            self.__ram[elem_key] = elem_value

    def __get_ram_list(self, ram_input: str) -> List[str]:
        ram_list: List[str] = []
        ram_split: List[str] = ram_input.splitlines()
        for line_raw in ram_split:
            if len(line_raw) < 3:
                continue

            line_upper = line_raw.upper()
            line_temp = line_upper

            line_temp = line_temp.replace('O', '0')
            # line_temp = line_temp.replace('I', '1')
            # line_temp = line_temp.replace('S', '8')

            line_result = line_temp

            ram_list.append(line_result)
        return ram_list
