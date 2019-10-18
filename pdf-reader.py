import pandas as pd
import tabula
import pdftotext

def extract_course_info(course):

    path = spec_to_get + ".pdf"
    filename = 'pdf_' + spec_to_get

    pdf_text = tabula.read_pdf(path, lattice=True, pandas_options={'header': None}, pages="all", multiple_tables=True)


    if(isinstance(pdf_text[0].iloc[0, 0], str)):
        print(pdf_text[0])
    else:
        with open(path, 'rb') as f:
            pdf = pdftotext.PDF(f)

        print(pdf[0])


if __name__ == '__main__':
    spec_to_get = input("Enter in the course specification you would like to scrape: ")
    # ../ProgrammeSpecifications/BScComputerScience
    # ../ProgrammeSpecifications/BScDigitalDegreeApprenticeship
    extract_course_info(spec_to_get)