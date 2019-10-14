import pandas as pd
import tabula

def extract_course_info(course):

    path = '../ProgrammeSpecifications/' + spec_to_get + ".pdf"
    filename = 'pdf_' + spec_to_get

    pdf_text = tabula.read_pdf(path, lattice=True, pandas_options={'header': None})

    specification_data = {}
    specification_data[pdf_text.iloc[0, 0]] = pdf_text.iloc[0, 1] # Programe Title
    specification_data['School'] = pdf_text.iloc[2, 1]
    specification_data['Degree Type'] = pdf_text.iloc[3, 1]
    specification_data['Location'] = pdf_text.iloc[9, 1]
    specification_data['Programme Length'] = pdf_text.iloc[10, 1]
    specification_data['Total Credits'] = pdf_text.iloc[11, 1]
    specification_data['Accredited'] = pdf_text.iloc[12, 1]

    #print(type(pdf_text.iloc[6]))

    for index, value in pdf_text.iloc[6].items():
        if value == 'X':
            if index == 1:
                specification_data['Attendance Type'] = "Full Time"
            elif index == 2:
                specification_data['Attendance Type'] = "Part Time"

    for index, value in pdf_text.iloc[8].items():
        if value == 'X':
            if index == 1:
                specification_data['Delivery Pattern'] = "Campus-based"
            elif index == 2:
                specification_data['Delivery Pattern'] = "Work-based"
            elif index == 3:
                specification_data['Delivery Pattern'] = "Online/distance"


    print(specification_data)

if __name__ == '__main__':
    spec_to_get = input("Enter in the course specification you would like to scrape: ")
    # BScComputerScience
    extract_course_info(spec_to_get)