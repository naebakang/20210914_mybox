import PyPDF2

watermark_file = open('watermark.pdf', 'rb')
pdf_watermark_reader = PyPDF2.PdfFileReader(watermark_file)

work_file = open('work.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(work_file)

pdf_writer = PyPDF2.PdfFileWriter()
for page_num in range(0, pdf_reader.numPages, 1):
    work_file_page = pdf_reader.getPage(page_num)
    work_file_page.mergePage(pdf_watermark_reader.getPage(0))

    pdf_writer.addPage(work_file_page)

    pdf_writer.extractText().encode("utf-8")

result_pdf_file = open('watermarked_cover.pdf', 'wb')
pdf_writer.write(result_pdf_file)

watermark_file.close()
work_file.close()
result_pdf_file.close()
