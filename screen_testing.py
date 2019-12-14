from pprint import pprint

import pyautogui

from src.bgcomp_reader.bcomp_reader import BCompReader
from src.bgcomp_reader.screen_config import ScreenConfig


def main():
    cfg = ScreenConfig()
    screenshot = pyautogui.screenshot(region = cfg.coords)

    bcomp_reader = BCompReader()
    flags, ram = bcomp_reader.get_flags_and_ram(cfg.flags_config, cfg.ram_size, screenshot)

    pprint(flags)
    pprint(ram)

    print('check 1')


if __name__ == '__main__':
    main()
