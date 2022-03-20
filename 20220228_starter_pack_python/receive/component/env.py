# File encoding: utf8


class Name:
    version = 'v115'
    list_code = [
        'A4',
    ]


class Parameter:
    """
    2개이상 함수에서 쓰이는 파라미터
    """
    def __init__(self):
        pass


class Directory(Parameter):
    project_output = r'/20201130_data/20220126_abcd/'
    result = project_output + 'result/'


class IndexKJW(Parameter):
    # trade
    ratio_max = 0.915


class HaveUnit(Parameter):
    min_investment_money = 1  # [dollar]
