import pandas as pd
import tabula

def extract_course_info(course):

    path = '../ProgrammeSpecifications/' + spec_to_get + ".pdf"
    filename = 'pdf_' + spec_to_get

    pdf_text = tabula.read_pdf(path, lattice=True, pandas_options={'header': None})
    print(pdf_text) # print pandas.core.frame.DataFrame
    print(pdf_text.iloc[0, [0, 1]])

    # tabula.convert_into(path, filename + '.tsv', 'tsv', lattice=True)
    # tabula.convert_into(path, filename + '.json', 'json', lattice=True)
    # tabula.convert_into(path, filename + '.csv', lattice=True)

if __name__ == '__main__':
    spec_to_get = input("Enter in the course specification you would like to scrape: ")
    # BScComputerScience
    extract_course_info(spec_to_get)