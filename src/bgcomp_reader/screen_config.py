from typing import Dict

from src.bgcomp_reader.size import Size
from src.utils.hash_list import HashList


class ScreenConfig:
    def __init__(self):
        self.delay_y: int = 0
        self.coords = tuple()
        self.flags_config: Dict[HashList, Size] = dict()
        self.ram_size: Size = Size(0, 0, 0, 0)
        self.__fill_in()

    def __fill_in(self):
        coords_input = (8, 62, 938, 580)
        self.coords = tuple([coord * 2 for coord in coords_input])

        self.delay_y = 84

        start_y_big = 170
        start_y_short = start_y_big + self.delay_y * 2

        start_x_left = 100
        start_x_right = 948

        width_big, height = 450, 50
        width_short = 300

        start_x_ar, start_y_ar = (1545, 965)

        self.flags_config[HashList(['AC', 'BR', 'PS', 'IR'])] = Size(start_x_left, start_y_big, width_big, height)
        self.flags_config[HashList(['DR', 'CR'])] = Size(start_x_right, start_y_big, width_big, height)
        self.flags_config[HashList(['IP', 'SP'])] = Size(start_x_right, start_y_short, width_short, height)
        self.flags_config[HashList(['AR'])] = Size(start_x_ar, start_y_ar, width_short, height)

        start_x_ram, start_y_ram = (1525, 105)
        width_ram, height_ram = (213, 805)
        self.ram_size = Size(start_x_ram, start_y_ram, width_ram, height_ram)


def main():
    temp = ScreenConfig()
    for key, value in temp.flags_config.items():
        print(key)
        print(value.height, value.width, value.x, value.y)
        print()


if __name__ == '__main__':
    main()
