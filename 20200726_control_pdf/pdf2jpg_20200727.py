# File encoding: UTF-8

from wand.image import Image as wi


class FileConvert:
    def __init__(self):
        pass

    @staticmethod
    def create_img_from_pdf():
        pdf = wi(filename="aaa.pdf", resolution=300)
        pdfimage = pdf.convert("png")
        i = 1
        for img in pdfimage.sequence:
            page = wi(image=img)
            page.save(filename=str(i)+".png")
            i += 1
