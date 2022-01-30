# package PyPDF2
import PyPDF2


filepath = './sample/dummy.pdf'
with open(filepath, 'rb') as file:
    print(file)
    reader = PyPDF2.PdfFileReader(file)
    print(reader.numPages)
    print(reader.getPage(0))

    page = reader.getPage(0)
    page.rotateClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)

    destinationfile = './sample/rotatedfile.pdf'
    with open(destinationfile, 'wb') as newfile:
        writer.write(newfile)

# filepath = './sample/twopage.pdf'
# with open(filepath, 'rb') as file2:
#     print(file2)
#     reader2 = PyPDF2.PdfFileReader(file2)
#     print(reader2.numPages)