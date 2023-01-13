# error 만들기
            top_error = true_top - prediction_top
            top_error_ratio = (top_error/true_top) * self.error_ratio_compensation_value
            bottom_error = true_bottom - prediction_bottom
            bottom_error_ratio = (bottom_error/true_bottom) * self.error_ratio_compensation_value

            # basic analysis
            top_error_ratio_average = numpy.mean(top_error_ratio)
            bottom_error_ratio_average = numpy.mean(bottom_error_ratio)

            top_error_ratio_variance = numpy.var(top_error_ratio)
            bottom_error_ratio_variance = numpy.var(bottom_error_ratio)

            top_error_ratio_standard_deviation = numpy.sqrt(top_error_ratio_variance)
            bottom_error_ratio_standard_deviation = numpy.sqrt(bottom_error_ratio_variance)

            covariance_top_bottom_error_ratio = numpy.mean(
                (top_error_ratio - top_error_ratio_average) * (bottom_error_ratio - bottom_error_ratio_average))

            kjw_rank = self.__get_kjw_rank(top_error_ratio, bottom_error_ratio)

            kjw_usability = self.__get_kjw_usability(prediction_top, prediction_bottom,
                                                     top_error_ratio, bottom_error_ratio)