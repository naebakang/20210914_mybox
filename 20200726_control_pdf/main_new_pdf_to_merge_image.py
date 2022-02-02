# File encoding: UTF-8

from wand.image import Image as wi
import os
import img2pdf
from img2pdf import convert


class Main:
    def __init__(self):
        ins_fileconvert = FileConvert()
        ins_watermark = Merge()

        ins_fileconvert.create_img_from_pdf()
        ins_watermark.create_watermarked_img()


class FileConvert:
    def __init__(self):
        pass

    @staticmethod
    def create_img_from_pdf():
        pdf = wi(filename="aaa.pdf", resolution=300)
        pdfimage = pdf.convert("jpg")
        i = 1
        for img in pdfimage.sequence:
            page = wi(image=img)
            page.save(filename='./output/' + str(i)+".jpg")
            i += 1


class Merge:
    def __init__(self):
        pass

    @staticmethod
    def create_watermarked_img():
        with open("out.pdf", "wb") as f:
            pdf_list = []
            for file in os.listdir('./output'):
                if file.endswith(".jpg"):
                    pdf_list.append(file)
            pdf = convert('1.jpg')
            f.write(pdf)


if __name__ is '__main__':
    ins_main = Main()
