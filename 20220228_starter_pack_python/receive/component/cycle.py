# File encoding: utf8

import time
import datetime

from component.phase.cp001 import CPhase001
from component.phase.cp002 import CPhase002
from component.load.l_cp005.alert import Gmail


class Cyclist:
    def __init__(self):
        self.ins_cp001 = CPhase001()
        self.ins_cp002 = CPhase002()
        self.ins_gmail = Gmail()

    def run(self):
        if self.__check_time():
            # try:
                self.__operation()

            # except Exception as e:
            #     contents = "error, 001, {}".format(e)
            #     print(contents)
            #     self.ins_gmail.run_send_error(contents=contents)
            #     time.sleep(60 * 30)
        else:
            print('-----time to rest-----')
            time.sleep(60*10)

    def __check_time(self):
        check_time = True
        time_now = datetime.datetime.now()
        if time_now.weekday() == 6:
            check_time = False
        else:
            if time_now.weekday() == 0:  # 0=월요일
                if time_now.hour < 10:
                    check_time = False
            elif time_now.weekday() == 5:  # 5=토요일
                if 8 <= time_now.hour:
                    check_time = False

        return check_time

    def __operation(self):
        self.ins_cp001.run()
        self.ins_cp002.run()


if __name__ == '__main__':
    ins = Cyclist()
    ins.run()
