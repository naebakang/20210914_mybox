# File encoding: utf8

"""
<any scripts>
"""

from component.once import Sprinter
from component.cycle import Cyclist


class App:
    def __init__(self):
        self.ins_sprinter = Sprinter()
        self.ins_cyclist = Cyclist()

    def run(self):
        print('-----Start-----')
        self.ins_sprinter.run()
        while 1:
                print('')
            # try:
                self.ins_cyclist.run()

            # except:
            #     self.ins_gmail.run_send_email(subject='error', contents=contents)
            #
            #     time.sleep(60 * 5)


if __name__ == '__main__':
    ins = App()
    ins.run()
