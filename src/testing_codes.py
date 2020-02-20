import re


class CodesController:
    def __init__(self):
        self.pattern_if = re.compile('F[a-fA-F0-9]{3}')
        self.pattern_io = re.compile('1[a-fA-F0-9]{3}')
        self.pattern_unaddressed = re.compile('0[a-fA-F0-9]{3}')
        self.pattern_addressed = re.compile('[a-fA-F0-9]{4}')

    def get_code_type(self, code: str) -> str:
        if self.pattern_if.match(code):
            return 'if'
        elif self.pattern_io.match(code):
            return 'io'
        elif self.pattern_unaddressed.match(code):
            return 'unaddressed'
        elif self.pattern_addressed.match(code):
            return 'addressed'
        else:
            return '!Команда не соответствует ни одному формату!'


def main():
    code = 'F400'

    codes_controller = CodesController()
    print(codes_controller.get_code_type(code))


if __name__ == '__main__':
    main()
