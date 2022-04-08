# File encoding: UTF-8

import os

from env import Name, Directory


def create_txt_annotation(dir_data, output_name):
    list_file = os.listdir(dir_data)
    list_file.remove('readme.txt')

    path_save = '.'
    path_file = '{}/{}'.format(path_save, output_name)
    with open(path_file, 'w') as wb:
        for i in list_file:
            a, b = i[-5:].split('.')
            if b == 'txt':
                pass
            else:
                wb.write(dir_data + '/' + str(i) + '\n')


ins_env_name = Name()
ins_env_directory = Directory()
create_txt_annotation(dir_data=ins_env_directory.training_validation_data, output_name=ins_env_name.annotation_train_val)
create_txt_annotation(dir_data=ins_env_directory.test_data, output_name=ins_env_name.annotation_test)
