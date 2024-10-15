# File encoding: utf8

import os
import shutil


class OneClickDeployment:
    def create_all_with_except(self, path_dir_from, path_dir_to, list_dir_except):
        list_item_top = os.listdir(path_dir_from)
        for item in list_item_top:
            if item in list_dir_except:
                pass
            else:
                self.__create_file(path_dir_from, path_dir_to, list_dir_except, item)

    def __create_file(self, path_dir_from, path_dir_to, list_dir_except, item):
        if item in list_dir_except:
            pass
        else:
            path_current = os.path.join(path_dir_from, item)
            path_current_to = path_current.replace(path_dir_from, path_dir_to)
            if os.path.isdir(path_current):
                if os.path.exists(path_current_to):
                    pass
                else:
                    os.makedirs(path_current_to)

                list_item = os.listdir(path_current)
                for item in list_item:
                    self.__create_file(path_current, path_current_to, list_dir_except, item)

            else:
                shutil.copyfile(path_current, path_current_to)


if __name__ == "__main__":
    ins = OneClickDeployment()
    path_dir_from = "/home/temp"
    path_dir_to = "/home/a/b/temp"
    list_dir_except = ["venv", ".idea", "env.py", "__pycache__"]
    ins.create_all_with_except(path_dir_from, path_dir_to, list_dir_except)
