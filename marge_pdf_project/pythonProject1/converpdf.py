from PyPDF2 import PdfMerger

pdfs=["one.pdf","two.pdf"]

merger=PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("merger.pdf")
merger.close()