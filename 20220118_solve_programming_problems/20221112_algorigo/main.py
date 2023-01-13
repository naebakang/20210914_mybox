# File encoding: utf8

from components.procedural.q_1 import EDA
from components.procedural.q_2 import Test
from components.procedural.q_3 import Cluster


class App:
    def __init__(self):
        self.ins_eda = EDA()
        self.ins_test = Test()
        self.ins_cluster = Cluster()

    def run(self):
        self.ins_eda.run()
        self.ins_test.run()
        self.ins_cluster.run()


if __name__ == '__main__':
    ins = App()
    ins.run()
