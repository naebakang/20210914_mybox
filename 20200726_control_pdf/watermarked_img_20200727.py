# File encoding: UTF-8

from wand.image import Image
import os

#./image/원본 폴더의 파일들 전부 가져오기
file_list = os.listdir('./')

img_list = []
for file_name in file_list:
    if file_name.endswith('png'):
        img_list.append(file_name)
print(img_list)

#워터마크로 사용할 이미지
w_mark = Image(filename = 'wartermark_20200727.png')
w_mark.sample(2000, 2000) #사이즈 변경함수

##실질적으로 워터마크를 넣는 코드
for filename in img_list:
    #사용할 이미지 파일을 img에 저장
    print("현재 처리하는 이미지 ",filename)
    img = Image(filename= './'+filename)

    #워터마크 적용 함수 watermark
    img.watermark(image=w_mark , transparency=0.95, left=300, top=600)
    img.save(filename='./new'+filename)