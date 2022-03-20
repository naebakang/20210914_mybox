# File encoding: utf8

"""
20220320_v001, 최초생성
"""

from component.once import Sprinter
from component.cycle import Cyclist


class App:
    def __init__(self):
        self.ins_sprinter = Sprinter()
        self.ins_cyclist = Cyclist()

    def run(self):
        print('-----Start App-----')
        self.ins_sprinter.run()
        while 1:
            print('')
            self.ins_cyclist.run()


if __name__ == '__main__':
    ins = App()
    ins.run()
