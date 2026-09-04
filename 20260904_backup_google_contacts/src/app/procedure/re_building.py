# File encoding: utf8

import os
import re
from datetime import datetime

import numpy
import pandas as pd

LIST_COL_PHONE = [
    ('Phone 1 - Label', 'Phone 1 - Value'),
    ('Phone 2 - Label', 'Phone 2 - Value'),
    ('Phone 3 - Label', 'Phone 3 - Value'),
    ('Phone 4 - Label', 'Phone 4 - Value'),
    ('Phone 5 - Label', 'Phone 5 - Value'),
]
LIST_PHONE_PREFIX_4 = ['0503', '0504', '0505', '0506', '0507', '0508', '0509']
LIST_PHONE_PREFIX_3 = [
    '010', '011', '016', '017', '018', '019',
    '031', '032', '033', '041', '042', '043', '044',
    '051', '052', '053', '054', '055', '061', '062', '063', '064',
    '070', '080',
]


class ReBuilding:
    def __init__(self):
        pass

    def run(self, path_file_old, path_dir_save):
        df = pd.read_csv(path_file_old)

        df = self.move_last_name_to_first_name(df)
        df = self.split_multi_phone_1(df)
        df = self.format_all_phone(df)
        df = self.fill_missing_phone_label(df)

        name_file_save = f'contacts_{datetime.now().strftime("%Y%m%d%H%M")}.csv'
        path_file_save = os.path.join(path_dir_save, name_file_save)
        df.to_csv(path_file_save, index=False)

    def move_last_name_to_first_name(self, df):
        mask = df['First Name'].isna() & df['Last Name'].notna()
        df.loc[mask, 'First Name'] = df.loc[mask, 'Last Name']
        df.loc[mask, 'Last Name'] = numpy.nan
        return df

    def split_multi_phone_1(self, df):
        mask = df['Phone 1 - Value'].astype(str).str.contains(' ::: ', na=False)

        for idx in df[mask].index:
            list_value = [value.strip() for value in df.at[idx, 'Phone 1 - Value'].split(' ::: ')]
            df.at[idx, 'Phone 1 - Value'] = list_value[0]

            for value_extra in list_value[1:]:
                col_label, col_value = self.find_empty_phone_slot(df, idx)
                if col_label is None:
                    break
                df.at[idx, col_label] = 'Work'
                df.at[idx, col_value] = value_extra

        return df

    def find_empty_phone_slot(self, df, idx):
        for col_label, col_value in LIST_COL_PHONE[1:]:
            if pd.isna(df.at[idx, col_value]):
                return col_label, col_value
        return None, None

    def format_all_phone(self, df):
        for _, col_value in LIST_COL_PHONE:
            df[col_value] = df[col_value].map(self.format_phone_value)
        return df

    def format_phone_value(self, value):
        if pd.isna(value):
            return value

        raw = str(value).strip()
        if raw == '':
            return value

        raw = re.sub(r'^\+?82[\s-]?', '0', raw)
        digits = re.sub(r'\D', '', raw)

        if raw.startswith('00') or len(digits) > 11:
            return raw

        for prefix in LIST_PHONE_PREFIX_4 + LIST_PHONE_PREFIX_3:
            if digits.startswith(prefix):
                remainder = digits[len(prefix):]
                return self.join_prefix_remainder(prefix, remainder, raw)

        if digits.startswith('02'):
            return self.join_prefix_remainder('02', digits[2:], raw)

        if digits.startswith('1') and len(digits) == 8:
            return f'{digits[:4]}-{digits[4:]}'

        return raw

    def join_prefix_remainder(self, prefix, remainder, raw):
        if len(remainder) == 7:
            return f'{prefix}-{remainder[:3]}-{remainder[3:]}'
        elif len(remainder) == 8:
            return f'{prefix}-{remainder[:4]}-{remainder[4:]}'
        return raw

    def fill_missing_phone_label(self, df):
        for col_label, col_value in LIST_COL_PHONE:
            mask = df[col_label].isna() & df[col_value].notna()
            df.loc[mask, col_label] = 'Mobile'
        return df


if __name__ == '__main__':
    ins = ReBuilding()
    path_file_old = '/home/kangdaepyo/Desktop/temp_20260904/contacts.csv'
    path_dir_save = '/home/kangdaepyo/Desktop/temp_20260904'
    ins.run(
        path_file_old=path_file_old,
        path_dir_save=path_dir_save,
    )
