# File encoding: utf8

import os
import shutil


class CopyProject:
    def create_all_with_except(self, path_dir_from, path_dir_to, list_except):
        list_item_top = os.listdir(path_dir_from)
        for item in list_item_top:
            path_current = os.path.join(path_dir_from, item)
            self.__create_file(path_dir_from, path_dir_to, list_except, path_current)

    def __create_file(self, path_dir_from, path_dir_to, list_except, path_current):
        basename = os.path.basename(path_current)
        if basename in list_except:
            pass
        else:
            # folder
            if os.path.isdir(path_current):
                # create
                path_dir_new = path_current.replace(path_dir_from, path_dir_to)
                if os.path.exists(path_dir_new):
                    pass
                else:
                    os.makedirs(path_dir_new)

                # exploration
                list_item = os.listdir(path_current)
                for item in list_item:
                    path_current_new = os.path.join(path_current, item)
                    self.__create_file(path_dir_from, path_dir_to, list_except, path_current_new)
            # file
            else:
                # create
                path_new_to = path_current.replace(path_dir_from, path_dir_to)
                # try:
                shutil.copyfile(path_current, path_new_to)
                # except:
                #     print("except~: {}".format(path_new_to))


if __name__ == "__main__":
    ins = CopyProject()
    path_dir_from = "/home/temp"
    path_dir_to = "/home/a/b/temp"
    list_except = [
        "venv",
        ".idea",
        "__pycache__",
        "build",
        "dist",
        "main.spec",
    ]
    ins.create_all_with_except(path_dir_from, path_dir_to, list_except)
