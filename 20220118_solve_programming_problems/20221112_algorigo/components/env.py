# File encoding: utf8


class Name:
    dic_total = {
        "Male": 0,
        "Female": 1,
        "Loyal Customer": 0,
        "disloyal Customer": 1,
        "Business travel": 0,
        "Personal Travel": 1,
        "Business": 0,
        "Eco Plus": 1,
        "Eco": 2,
        "neutral or dissatisfied": 0,
        "satisfied": 1,
    }
    dic_gender = {
        "Male": 0,
        "Female": 1,
    }

    dic_customer_type = {
        "Loyal Customer": 0,
        "disloyal Customer": 1,
    }

    dic_type_of_travel = {
        "Business travel": 0,
        "Personal Travel": 1,
    }

    dic_class = {
        "Business": 0,
        "Eco Plus": 1,
        "Eco": 2,
    }

    dic_satisfaction = {
        "neutral or dissatisfied": 0,
        "satisfied": 1,
    }


class Parameter:
    """
    2개이상 함수에서 쓰이는 파라미터
    """
    def __init__(self):
        pass


class PathDirectory(Parameter):
    project_output = '/20200619_research_data/20220118_solve_programming_problems/20221112_algorigo'
    raw_data = project_output + "/data"
