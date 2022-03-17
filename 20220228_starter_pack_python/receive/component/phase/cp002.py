# File encoding: utf8

from component.c001 import Save001
from component.c001 import Save002


class Cyclist:
    def __init__(self):
        self.ins_save001 = Save001()
        self.ins_save002 = Save002()

    def run(self):
        self.ins_save001.create_any()
        self.ins_save002.create_any()


if __name__ == '__main__':
    ins = Cyclist()
    ins.run()
