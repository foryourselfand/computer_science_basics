from pprint import pprint
from typing import Dict, List, Tuple

import pytesseract
import pyautogui
from PIL.Image import Image

from src.bcomp_reader import BCompReader
from src.screen_config import ScreenConfig
from src.size import Size


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
