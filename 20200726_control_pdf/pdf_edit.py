# File encoding: UTF-8

import os
from PyPDF2 import PdfFileReader, PdfFileWriter

file_name ='/home/kangdaepyo/Desktop/a.pdf'
pdf= PdfFileReader(open(file_name, 'rb'))


def create_new_pdf(total_page, new_name):
    new_pdf = PdfFileWriter()

    for page in total_page:
        new_pdf.addPage(pdf.getPage(page))
        with open(new_name, 'wb') as wb:
            new_pdf.write(wb)


total_page = [0, 1, 2, 3, 5, 8]
new_name = 'a.pdf'
create_new_pdf(total_page, new_name)

total_page = [0, 1, 2, 3, 6, 7]
new_name = 'b.pdf'
create_new_pdf(total_page, new_name)
