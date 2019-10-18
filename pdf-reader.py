import pandas as pd
import tabula
import pdftotext

def extract_course_info(course):

    path = spec_to_get + ".pdf"
    filename = 'pdf_' + spec_to_get

    pdf_text = tabula.read_pdf(path, lattice=True, pandas_options={'header': None}, pages="all", multiple_tables=True)
    
    specification_data = {}

    if(isinstance(pdf_text[0].iloc[0, 0], str)):
        for index, page in enumerate(pdf_text):
            # page = page in PDF file
            # index = page no i.e 0 = 1, 1 = 2, etc
            if(index == 0):
                specification_data[page.iloc[0, 0]] = page.iloc[0, 1] # Programe Title
                specification_data['School of Study'] = page.iloc[2, 1]
                specification_data['Degree Type'] = page.iloc[3, 1]
                specification_data['Location'] = page.iloc[9, 1]
                specification_data['Programme Length'] = page.iloc[10, 1]
                specification_data['Total Credits'] = page.iloc[11, 1]
                specification_data['Accredited'] = page.iloc[12, 1]
    else:
        with open(path, 'rb') as f:
            pdf = pdftotext.PDF(f)
            for index, page in enumerate(pdf):
                if(index == 0):
                    specification_data = page


    print(specification_data)


if __name__ == '__main__':
    spec_to_get = input("Enter in the course specification you would like to scrape: ")
    # ../ProgrammeSpecifications/BScComputerScience
    # ../ProgrammeSpecifications/BScDigitalDegreeApprenticeship
    extract_course_info(spec_to_get)