import re


class CodesController:
    def __init__(self):
        self.pattern_ifs = re.compile('F[a-fA-F0-9]{3}')
        self.pattern_io = re.compile('1[a-fA-F0-9]{3}')
        self.pattern_unaddressed = re.compile('0[a-fA-F0-9]{3}')
        self.pattern_addressed = re.compile('[a-fA-F0-9]{4}')
    
    def get_code_type(self, code: str) -> str:
        if self.pattern_ifs.match(code):
            return 'Ветвления'
        elif self.pattern_io.match(code):
            return 'Ввода-вывода'
        elif self.pattern_unaddressed.match(code):
            return 'Безадресная'
        elif self.pattern_addressed.match(code):
            return 'Адресная'
        else:
            return '!Комманда не соответствует ни одному формату!'


def main():
    code = 'F400'
    
    codes_controller = CodesController()
    print(codes_controller.get_code_type(code))


if __name__ == '__main__':
    main()
