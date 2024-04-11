# File encoding: utf8

"""
Description
"""

from components.function.base import Memory, ETC

from components.env import Name, PathDirectory, PathFile, IndexKJW, HaveUnit


class Temp:
    def __init__(self):
        self.ins_base_memory = Memory()
        self.ins_base_etc = ETC()

        self.ins_env_name = Name()
        self.ins_env_pathdirectory = PathDirectory()
        self.ins_env_pathfile = PathFile()
        self.ins_env_indexkjw = IndexKJW()
        self.ins_env_haveunit = HaveUnit()


if __name__ == "__main__":
    ins = Temp()
