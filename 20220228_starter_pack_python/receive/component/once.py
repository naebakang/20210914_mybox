# File encoding: utf8

from component.phase.op001 import OPhase001
from component.phase.op002 import OPhase002


class Sprinter:
    def __init__(self):
        self.ins_op001 = OPhase001()
        self.ins_op002 = OPhase002()

    def run(self):
        self.ins_op001.run()
        self.ins_op002.run()
