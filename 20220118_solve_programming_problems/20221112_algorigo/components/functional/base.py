# File encoding: utf8

import os
import time
import numpy
import pandas
import json
import datetime
import ast


class FileSystem:
    def __init__(self):
        pass

    @staticmethod
    def get_recent_file_name(directory, file_group_name, len_now_time, extension=None):
        # parameter
        directory = str(directory)
        file_group_name = str(file_group_name)
        len_now_time = int(len_now_time)

        file_name_list = os.listdir(directory)
        list_file_name = []
        for i in file_name_list:
            namee, ext = os.path.splitext(i)
            list_file_name.append(namee)

        want_index_list = []
        for i in list_file_name:
            if file_group_name in i:
                want_index_list.append(i)

        # 숫자만 축출
        digit = []
        for n in want_index_list:
            i = n[-len_now_time:]
            digit_str = ''
            for ii in i:
                if ii.isdigit():
                    digit_str = digit_str + ii
                else:
                    pass
            digit.append(digit_str)

        # 날짜에 대한 것만 축출
        nowdate_list = []
        for i in digit:
            nowdate_list.append(i[-len_now_time:])

        # 날짜를 정수로 변환
        nowdate_list_int = []
        for i in nowdate_list:
            nowdate_list_int.append(int(i))

        # 가장 큰 정수를 가진 항목의 위치를 구함
        i = 0
        for i in range(0, len(nowdate_list_int)):
            if str(max(nowdate_list_int)) in nowdate_list[i]:
                break

        if extension == None:
            anw = want_index_list[i]
        else:
            anw = want_index_list[i]

        return anw

    @staticmethod  # 이거 부터 만들자
    def get_recent_file_name_not_df0(n, directory, file_group_name, len_now_time, extension=None):
        # parameter
        directory = str(directory)
        file_group_name = str(file_group_name)
        len_now_time = int(len_now_time)

        file_name_list = os.listdir(directory)
        list_file_name = []
        for i in file_name_list:
            namee, ext = os.path.splitext(i)
            list_file_name.append(namee)

        want_index_list = []
        for i in list_file_name:
            if file_group_name in i:
                want_index_list.append(i)

        # 숫자만 축출
        digit = []
        for n in want_index_list:
            i = n[-len_now_time:]
            digit_str = ''
            for ii in i:
                if ii.isdigit():
                    digit_str = digit_str + ii
                else:
                    pass
            digit.append(digit_str)

        # 날짜에 대한 것만 축출
        nowdate_list = []
        for i in digit:
            nowdate_list.append(i[-len_now_time:])

        # 날짜를 정수로 변환
        nowdate_list_int = []
        for i in nowdate_list:
            nowdate_list_int.append(int(i))

        def get_index(n, nowdate_list_int):
            for ii in range(n):
                # 가장 큰 정수를 가진 항목의 위치를 구함
                i = 0
                for i in range(0, len(nowdate_list_int)):
                    if str(max(nowdate_list_int)) in nowdate_list[i]:
                        break

            return i

        i = get_index(n, nowdate_list_int)

        if extension == None:
            anw = want_index_list[i]
        else:
            anw = want_index_list[i]

        return anw


class Memory:
    def __init__(self):
        self.ins_filesystem = FileSystem()

    def create_cover_json(self, directory, file_name, dic):
        dic_str = {}
        for key, value in dic.items():
            dic_str[key] = str(value)
        path_file = os.path.join(directory, file_name + ".json")
        with open(path_file, 'w') as f:
            json.dump(dic_str, f)

    def create_cover_feather(self, directory, file_name, df):
        pandas.options.display.float_format = '{:.4f}'.format
        df = df.reset_index(drop=True)  # "index" 가 0 부터 1씩 아래로 늘어나도록 수정
        if len(df) == 0:
            df['0'] = numpy.nan

        df = df.astype(str)

        path_file = os.path.join(directory, file_name + ".ftr")
        df.to_feather(path=path_file)

    def get_cover_saved_data(self, directory, file_name, extension=None):
        saved_data = None
        if extension == None:
            pass

        elif extension == 'json':
            path_file = os.path.join(directory, file_name + ".json")
            with open(path_file, 'r') as f:
                saved_data = json.load(f)

            for key, value in saved_data.items():
                if len(value) == 0:
                    pass
                else:
                    if value[0] == "{" or value[0] == "[" or value[0] == "(":
                        saved_data[key] = ast.literal_eval(value)

        elif extension == 'ftr':
            path_file = os.path.join(directory, file_name + ".ftr")
            time.sleep(0.2)
            saved_data = pandas.read_feather(path=path_file, columns=None, use_threads=True, storage_options=None)

        elif extension == 'csv':
            filepath_or_buffer = os.path.join(directory, file_name + ".csv")
            saved_data = pandas.read_csv(filepath_or_buffer=filepath_or_buffer,
                                         header=0,
                                         # index_col='index',
                                         dtype={
                                             'minprice': str,
                                             'minqty': str,
                                             'minnotional': str
                                         },
                                         # na_values='NaN',
                                         thousands=',')

        elif extension == 'xlsx':
            io = os.path.join(directory, file_name + ".xlsx")
            saved_data = pandas.read_excel(
                io,
                header=0,
                index_col='index',
                dtype={
                    'minprice': str,
                    'minqty': str,
                    'minnotional': str
                },
                na_values='NaN',
                thousands=',',
            )

        return saved_data

    def create_cumulate_feather(self, directory, file_name, df):
        pandas.options.display.float_format = '{:.4f}'.format
        df = df.reset_index(drop=True)  # "index" 가 0 부터 1씩 아래로 늘어나도록 수정
        if len(df) == 0:
            df['0'] = numpy.nan

        df = df.astype(str)

        now_time = datetime.datetime.now().strftime('%Y%m%d%H%M')
        file_name = '{}_{}'.format(file_name, now_time)
        path_file = os.path.join(directory, file_name + ".ftr")
        df.to_feather(path=path_file)

    def create_cumulate_csv(self, directory, file_name, df):
        pandas.options.display.float_format = '{:.4f}'.format
        df = df.reset_index(drop=True)  # "index" 가 0 부터 1씩 아래로 늘어나도록 수정
        if len(df) == 0:
            df['0'] = numpy.nan

        df = df.astype(str)

        now_time = datetime.datetime.now().strftime('%Y%m%d%H%M')
        file_name = '{}_{}'.format(file_name, now_time)
        path_or_buf = os.path.join(directory, file_name + ".csv")
        df.to_csv(path_or_buf=path_or_buf,
                  float_format='0.8f',
                  index=True,
                  index_label='index')

    def get_cumulate_recent_saved_data(self, len_now_time, directory, file_group_name, extension=None):
        saved_data = None

        file_name = self.ins_filesystem.get_recent_file_name(directory=directory,
                                                             file_group_name=file_group_name,
                                                             len_now_time=len_now_time,
                                                             extension=extension)
        filepath_or_buffer = os.path.join(directory, file_name + "." + extension)
        if extension == 'csv':
            saved_data = pandas.read_csv(filepath_or_buffer=filepath_or_buffer,
                                         header=0,
                                         index_col='index',
                                         dtype={
                                             'minprice': str,
                                             'minqty': str,
                                             'minnotional': str
                                         },
                                         na_values='NaN',
                                         thousands=',')
        elif extension == 'ftr':
            saved_data = pandas.read_feather(path=filepath_or_buffer, columns=None, use_threads=True, storage_options=None)

        return saved_data
