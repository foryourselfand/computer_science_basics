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

    screenshot = pyautogui.screenshot('screenshot.png', region = coords)

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

    pprint(flags)


if __name__ == '__main__':
    main()
