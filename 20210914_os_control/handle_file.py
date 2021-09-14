# File encoding: UTF-8

import os

# 주어진 디렉토리에 있는 항목들의 이름을 담고 있는 리스트를 반환합니다.
# 리스트는 임의의 순서대로 나열됩니다.
file_path = r'D:\20210329_data\yolo4_Dataset Example\img'
file_names = os.listdir(file_path)
file_names
