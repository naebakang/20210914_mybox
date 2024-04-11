# File encoding: utf8


class Name:
    version = '20230802_v001'


class Path:
    """
    2개이상 함수에서 쓰이는 파라미터
    """
    def __init__(self):
        pass


class PathDirectory(Path):
    project_output = '/test'


class PathFile(Path):
    file = PathDirectory.project_output + "/test.csv"


class Digit:
    pass


class IndexKJW(Digit):
    # shell
    num_of_step = 20


class HaveUnit(Digit):
    min_investment_money = 5  # [dollar]
