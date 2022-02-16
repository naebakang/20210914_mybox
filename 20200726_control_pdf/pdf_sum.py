# File encoding: utf8

from PyPDF2 import PdfFileReader, PdfFileWriter

file_name ='/home/kangdaepyo/Desktop/a.pdf'
pdf_a = PdfFileReader(open(file_name, 'rb'))
file_name ='/home/kangdaepyo/Desktop/b.pdf'
pdf_b = PdfFileReader(open(file_name, 'rb'))


new_pdf = PdfFileWriter()
for page in range(4):
    new_pdf.addPage(pdf_a.getPage(page))
    with open('/home/kangdaepyo/Desktop/new.pdf', 'wb') as wb:
        new_pdf.write(wb)

for page in range(4):
    new_pdf.addPage(pdf_b.getPage(page))
    with open('/home/kangdaepyo/Desktop/new.pdf', 'wb') as wb:
        new_pdf.write(wb)
