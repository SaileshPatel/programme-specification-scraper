from PyPDF2 import PdfFileReader

# - Author: Mike
# - Date: 07/06/20148
# - Title: An Intro to PyPDF2
# - Type: Source Code Tutorial
# - Availability: http://www.blog.pythonlibrary.org/2018/06/07/an-intro-to-pypdf2/

def extract_text(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(path, False)


        for num in range(pdf.getNumPages()):
            print(pdf.getPage(num).extractText())

        # page = pdf.getPage(1)
        # print(page.extractText())


if __name__ == '__main__':
    extract_text('../ProgrammeSpecifications/BScComputerScience.pdf')