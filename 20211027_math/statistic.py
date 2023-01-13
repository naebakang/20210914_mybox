# File encoding: UTF-8

import numpy


class Statistician:
    def __init__(self):
        pass

    @staticmethod
    def get_class_and_relative_frequency(data):
        # parameter
        num_of_class_value = int(100)  # 100[-]

        # input variable
        data = data

        if len(data) < 3:
            statistics_class = 'error: len(data) < 3'
            class_value = 'error: len(data) < 3'
            relative_frequency = 'error: len(data) < 3'
        else:
            # 계급 정하기
            data_max = max(data)
            data_min = min(data)
            statistics_class = numpy.linspace(start=data_min, stop=data_max, num=num_of_class_value, endpoint=True,
                                              dtype=float)

            # 도수 & 계급값
            frequency = numpy.zeros(len(statistics_class) - 1, dtype=int)
            class_value = numpy.zeros(len(statistics_class) - 1, dtype=float)
            for ii in range(len(statistics_class) - 1):
                class_value[ii] = (statistics_class[ii] + statistics_class[ii + 1]) / 2
                for iii in data:
                    if statistics_class[ii] <= iii < statistics_class[ii + 1]:
                        frequency[ii] += 1

            # 가장 큰 값은 도수에 반영이 안 되었으므로 보정해준다.
            frequency[-1] += 1

            # 상대도수
            relative_frequency = frequency / sum(frequency)

        return statistics_class, class_value, relative_frequency

    def get_xy_for_relative_frequency_polygon(self, data):
        # input variable
        data = data

        statistics_class, class_value, relative_frequency = self.get_class_and_relative_frequency(data)

        class_width = statistics_class[1] - statistics_class[0]

        # x, y
        x = numpy.zeros(len(relative_frequency) + 2, dtype=float)
        y = numpy.zeros(len(relative_frequency) + 2, dtype=float)
        x[0] = class_value[0] - (class_value[1] - class_value[0])
        x[-1] = class_value[-1] + (class_value[1] - class_value[0])
        y[0] = 0
        y[-1] = 0
        for ii in range(len(relative_frequency)):
            x[ii + 1] = class_value[ii]
            y[ii + 1] = relative_frequency[ii]/class_width

        return x, y

    def get_class_upper(self, data, cumulative_probability):
        # input_variable
        data = data
        cumulative_rate = float(cumulative_probability)

        statistics_class, class_value, relative_frequency = self.get_class_and_relative_frequency(data)

        # 누적상대도수
        cumulative_relative_frequency = [relative_frequency[0]]
        for ii in range(len(relative_frequency) - 1):
            cumulative_relative_frequency.append(cumulative_relative_frequency[ii] + relative_frequency[ii + 1])

        # 원하는 누적확률을 만족하는 계급의 상한값 구하기
        class_upper = 0
        for ii in range(len(cumulative_relative_frequency)):
            if cumulative_probability <= cumulative_relative_frequency[ii]:
                class_upper = statistics_class[ii + 1]
                break

        return float(class_upper)

    # def regression(self):
    #     # error2_ratio = a*error1_ratio + b
    #
    #     # ab_of_error2_equl_a_mul_error1_plus_b
    #     if covariance_error1_2_ratio <= 0:
    #         a_of_error2_equl_a_mul_error1_plus_b = numpy.nan
    #         b_of_error2_equl_a_mul_error1_plus_b = numpy.nan
    #
    #     else:
    #         x = numpy.concatenate((numpy.array([error1_ratio]), numpy.ones_like(numpy.array([error1_ratio]))), axis=0)
    #         y = numpy.array([error2_ratio])
    #
    #         ab, residuals, rank, s = numpy.linalg.lstsq(x.T, y.T, rcond=None)
    #
    #         a_of_error2_equl_a_mul_error1_plus_b = ab[0][0]
    #         b_of_error2_equl_a_mul_error1_plus_b = ab[1][0]
    #
    #     # b_of_error2_equl_a_mul_error1_plus_b 값 조정
    #     while 1:
    #         count = 0
    #         for ii in range(len(error1_ratio)):
    #             if a_of_error2_equl_a_mul_error1_plus_b * error1_ratio.values[ii] + b_of_error2_equl_a_mul_error1_plus_b \
    #                     < error2_ratio.values[ii]:
    #                 count += 1
    #
    #         if upper_distribution_ratio < count / len(error1_ratio):
    #             b_of_error2_equl_a_mul_error1_plus_b = b_of_error2_equl_a_mul_error1_plus_b \
    #                                                    + (max(error2_ratio) - min(error2_ratio)) / error2_ratio_stair
    #         else:
    #             break
