# File encoding: utf8

import pandas
import numpy

from components.functional.base import Memory

from components.env import Name, PathDirectory


class EDA:
    def __init__(self):
        self.ins_base_memory = Memory()

        self.ins_env_name = Name()
        self.ins_env_pathdirectory = PathDirectory()

    def run(self):
        data_train = self.ins_base_memory.get_cover_saved_data(
            directory=self.ins_env_pathdirectory.raw_data,
            file_name="train",
            extension="csv"
        )

        data_test = self.ins_base_memory.get_cover_saved_data(
            directory=self.ins_env_pathdirectory.raw_data,
            file_name="test",
            extension="csv"
        )

        data_unlabeled = self.ins_base_memory.get_cover_saved_data(
            directory=self.ins_env_pathdirectory.raw_data,
            file_name="unlabeled",
            extension="csv"
        )

        data_train = data_train.dropna(axis=1)

        data_train = self.__get_df_only_num(data_train)
        data_test = self.__get_df_only_num(data_test)
        data_unlabeled = self.__get_df_only_num(data_unlabeled)

        col_label_1 = data_train.loc[:, "satisfaction"]
        col_label_2 = data_test.loc[:, "satisfaction"]
        col_label = pandas.concat([col_label_1, col_label_2], axis=0)

        df = pandas.DataFrame()
        for i in range(1, data_test.shape[1]):
            if i < 12:
                col_1 = data_train.iloc[:, i]
                col_2 = data_test.iloc[:, i]
                col = pandas.concat([col_1, col_2], axis=0)

                col_label_1 = data_train.loc[:, "satisfaction"]
                col_label_2 = data_test.loc[:, "satisfaction"]
                col_label = pandas.concat([col_label_1, col_label_2], axis=0)
            else:
                col = data_test.iloc[:, i]
                col_label = data_test.loc[:, "satisfaction"]

            covariance = self.__get_correlation_coefficient(col, col_label)

            df_new = pandas.DataFrame(
                [
                    [
                        data_test.columns[i],
                        covariance
                    ]
                ],
                columns=[
                    "vector",
                    "covariance"
                ]
            )

            df = pandas.concat([df, df_new], axis=0)

        self.ins_base_memory.create_cumulate_csv(
            directory=self.ins_env_pathdirectory.project_output,
            file_name="covariance",
            df=df
        )

    def __get_df_only_num(self, df):
        for key, value in self.ins_env_name.dic_total.items():
            df = df.replace(key, value)

        df_only_num = df

        return df_only_num

    def __get_correlation_coefficient(self, vector_1, vector_2):
        # basic analysis
        vector_1_average = numpy.mean(vector_1)
        vector_2_average = numpy.mean(vector_2)

        covariance = numpy.mean((vector_1 - vector_1_average) * (vector_2 - vector_2_average))

        vector_1_variance = numpy.var(vector_1)
        vector_2_variance = numpy.var(vector_2)
        denominator = numpy.sqrt(vector_1_variance*vector_2_variance)

        correlation_coefficient = covariance/denominator

        return correlation_coefficient


if __name__ == "__main__":
    ins = EDA()
    ins.run()
