from pprint import pprint
from typing import Dict, List

import pytesseract
import pyautogui


def read_flags(start_x: int, start_y: int,
               width: int, height: int,
               names: List[str],
               screenshot, flags: Dict[str, str], delay_y: int):
    for y_multiplier, name_key in enumerate(names):
        part_temp = screenshot.crop(
            (start_x, start_y + delay_y * y_multiplier, start_x + width, start_y + height + delay_y * y_multiplier))
        digits_temp = pytesseract.image_to_string(part_temp)
        flags[name_key] = digits_temp


def main():
    coords_input = (8, 62, 938, 580)
    coords = tuple([coord * 2 for coord in coords_input])

    screenshot = pyautogui.screenshot('images/screenshot-4.png', region = coords)

    delay_y = 84

    start_y_big = 170
    start_y_short = start_y_big + delay_y * 2

    start_x_left = 100
    start_x_right = 948

    width_big, height = 450, 50
    width_short = 300

    flags: Dict[str, str] = dict()

    names_left: List[str] = ['AC', 'BR', 'PS', 'IR']
    names_right_big: List[str] = ['DR', 'CR']
    names_right_short: List[str] = ['IP', 'SP']

    read_flags(start_x_left, start_y_big,
               width_big, height,
               names_left,
               screenshot, flags, delay_y)
    read_flags(start_x_right, start_y_big,
               width_big, height,
               names_right_big,
               screenshot, flags, delay_y)
    read_flags(start_x_right, start_y_short,
               width_short, height,
               names_right_short,
               screenshot, flags, delay_y)
    # pprint(flags)

    start_x_ram, start_y_ram = (1525, 105)
    width_ram, height_ram = (213, 805)
    # ram_image = screenshot.crop((start_x_ram, start_y_ram,
    #                              start_x_ram + width_ram, start_y_ram + height_ram))
    #
    # allowed_digits = '0123456789'
    # allowed_chars_lower = 'abcdef'
    # allowed_chars_upper = 'ABCDEF'
    # allowed_chars = allowed_digits + allowed_chars_lower + allowed_chars_upper
    # config_temp = f'tessedit_char_whitelist={allowed_chars}'
    #
    # ram_str = pytesseract.image_to_string(ram_image, lang = 'eng', config = config_temp)
    # ram_list = get_processed_ram(ram_str)
    # ram_dict = get_ram_dict(ram_list)
    # pprint(ram_dict)

    start_x_ar, start_y_ar = (1545, 965)
    ar_image = screenshot.crop((start_x_ar, start_y_ar,
                                start_x_ar + width_short, start_y_ar + height))
    ar_image.save('images/ar-4.png')


def get_processed_ram(ram_input: str) -> List[str]:
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


def get_ram_dict(ram_list: List[str]) -> Dict[str, str]:
    ram_dict: Dict[str, str] = dict()

    len_half = len(ram_list) // 2
    for elem_key, elem_value in zip(ram_list[:len_half], ram_list[len_half:]):
        ram_dict[elem_key] = elem_value

    return ram_dict


if __name__ == '__main__':
    main()
