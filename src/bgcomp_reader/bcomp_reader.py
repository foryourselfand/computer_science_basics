import operator
from collections import defaultdict
from pprint import pprint
from typing import Dict, List, Tuple

import pyautogui
from PIL.Image import Image
from pytesseract import pytesseract

from src.bgcomp_reader.screen_config import ScreenConfig
from src.utils.helper import Helper
from src.words.words_writer import WordsWriter


class BCompReader:
    def __init__(self):
        self.__allowed = '0123456789ABCDEF'
        self.__cfg = ScreenConfig()
        self.__flags: Dict[str, str] = dict()
        self.__ram: Dict[str, str] = dict()
        self.__delay_y: int = 84
        self.__screenshot: Image = Image()
    
    def get_flags_and_ram(self) \
            -> Tuple[Dict[str, str], Dict[str, str]]:
        self.process_computer()
        return self.get_flags(), self.get_ram()
    
    def process_computer(self):
        self.__flags = dict()
        self.__ram = dict()
        
        self.__screenshot = pyautogui.screenshot(region = self.__cfg.coords)
        # self.__screenshot.save(f'{get_project_root()}/images/tmp/{self.n}.png')
        # self.n += 1
        self.__process_flags()
        self.__process_ram()
        
        self.__fix_ram()
        # self.__reduce_ram()
        
        if not self.__check_ram_values():
            print('BUT HURT')
    
    def get_flags(self):
        return self.__flags
    
    def get_ram(self):
        return self.__ram

    # def __reduce_ram(self):
    #     new_ram: Dict[str, str] = dict()
    #     for key, value in self.__ram.items():
    #         if value == '0000':
    #             continue
    #         new_ram[key] = value
    #     self.__ram = new_ram.copy()
    #
    def __process_flags(self):
        for names, size in self.__cfg.flags_config.items():
            for y_multiplier, name_key in enumerate(names):
                text_temp = self.__read_flag(size.x, size.y, size.width, size.height, y_multiplier)
                self.__flags[name_key] = text_temp.replace(' ', '')
    
    def __fix_ram(self):
        if self.__check_ram_keys():
            return
        print('SOMETHING BAD')
        first: Dict[str, int] = defaultdict(int)
        second: Dict[str, int] = defaultdict(int)
        
        for key in self.__ram.keys():
            first[key[0]] += 1
            second[key[1]] += 1
        first_sorted = sorted(first.items(), key = operator.itemgetter(0))
        second_sorted = sorted(second.items(), key = operator.itemgetter(0))
        
        print('first_sorted')
        pprint(first_sorted)
        
        print('second_sorted')
        pprint(second_sorted)
        
        first_common = first_sorted[0][0]
        second_common = second_sorted[0][0]
        
        print('first_common:', first_common)
        print('second_common:', second_common)
        
        print('ram_before')
        pprint(self.__ram)
        print()
        
        new_ram: Dict[str, str] = dict()
        for old_key, digit in zip(self.__ram.keys(), self.__allowed):
            print('old_key:', old_key)
            new_key = f'{first_common}{second_common}{digit}'
            print('new_key:', new_key)
            print()
            new_ram[new_key] = self.__ram[old_key]
        self.__ram = new_ram
        
        print('ram_after')
        pprint(self.__ram)
        print()
    
    def __check_collection(self, collection):
        for elem in collection:
            for elem_part in elem:
                if elem_part not in self.__allowed:
                    print(f'STUPID -> {elem_part}')
                    return False
        return True
    
    def __check_ram_keys(self):
        return self.__check_collection(self.__ram.keys())
    
    def __check_ram_values(self):
        return self.__check_collection(self.__ram.values())
    
    def __process_ram(self):
        ram_image = self.__screenshot.crop((self.__cfg.ram_size.x, self.__cfg.ram_size.y,
                                            self.__cfg.ram_size.x + self.__cfg.ram_size.width,
                                            self.__cfg.ram_size.y + self.__cfg.ram_size.height))
        
        ram_left = ram_image.crop((0, 0,
                                   95, self.__cfg.ram_size.height))
        ram_right = ram_image.crop((100, 0,
                                    self.__cfg.ram_size.width, self.__cfg.ram_size.height))
        
        # ram_image.save(f'{get_project_root()}/images/ram_temp.png')
        # ram_left.save(f'{get_project_root()}/images/ram_left.png')
        # ram_right.save(f'{get_project_root()}/images/ram_right.png')
        
        allowed_digits = '0123456789'
        # allowed_chars_lower = 'abcdef'
        allowed_chars_upper = 'ABCDEF'
        allowed_chars = allowed_digits + allowed_chars_upper
        config_temp = f"-c tessedit_char_whitelist={allowed_chars}"
        
        ram_left_str = pytesseract.image_to_string(ram_left, config = config_temp)
        ram_right_str = pytesseract.image_to_string(ram_right, config = config_temp)
        
        ram_left_list = []
        for ram_left_temp in ram_left_str.splitlines():
            if ram_left_temp == '':
                continue
            ram_left_list.append(ram_left_temp)
        
        ram_right_list = []
        for ram_right_temp in ram_right_str.splitlines():
            if ram_right_temp == '':
                continue
            ram_right_list.append(ram_right_temp)
        
        # print('ram_left_str')
        # print(ram_left_str)
        # print()
        #
        # print('ram_right_str')
        # print(ram_right_str)
        # print()
        
        for key, value in zip(ram_left_list, ram_right_list):
            self.__ram[key] = value
    
    def __read_flag(self, x: int, y: int, width: int, height: int, y_multiplier: int, name: str) -> str:
        screenshot_part: Image = self.__screenshot.crop((x, y + self.__delay_y * y_multiplier,
                                                         x + width, y + height + self.__delay_y * y_multiplier))
        screenshot_part.save(f'{Helper.get_project_root()}/images/{name}.png')
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


def main():
    words_writer = WordsWriter()
    words_writer.switch_to_next_window()
    
    bcomp_reader = BCompReader()
    
    flags, ram = bcomp_reader.get_flags_and_ram()
    
    pprint(flags)
    pprint(ram)


if __name__ == '__main__':
    main()
