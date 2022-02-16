# File encoding: UTF-8

from wand.image import Image as wi
from wand.image import Image
import os


class Main:
    def __init__(self):
        ins_fileconvert = FileConvert()
        ins_watermark = WaterMark()

        ins_fileconvert.create_img_from_pdf()
        ins_watermark.create_watermarked_img()


class FileConvert:
    def __init__(self):
        pass

    @staticmethod
    def create_img_from_pdf():
        pdf = wi(filename="document.pdf", resolution=300)
        pdfimage = pdf.convert("png")
        i = 1
        for img in pdfimage.sequence:
            page = wi(image=img)
            page.save(filename=str(i)+".png")
            i += 1


class WaterMark:
    def __init__(self):
        self.watermark = 'wartermark_20200727.png'

    def create_watermarked_img(self):
        # 현재 폴더의 파일들 전부 가져오기
        file_list = os.listdir('./')

        img_list = []
        for file_name in file_list:
            if file_name.endswith('png'):
                img_list.append(file_name)

        # 워터마크로 사용할 이미지
        del img_list[img_list.index(self.watermark)]
        w_mark = Image(filename=self.watermark)
        w_mark.sample(2000, 2000)  # 사이즈 변경함수

        # 워터마크를 넣는 코드
        for filename in img_list:
            # 사용할 이미지 파일을 img에 저장
            print("현재 처리하는 이미지 ", filename)
            img = Image(filename='./' + filename)

            # 워터마크 적용 함수 watermark
            img.watermark(image=w_mark, transparency=0.95, left=300, top=720)
            img.save(filename='./blog' + filename)


if __name__ is '__main__':
    ins_main = Main()
