import pandas as pd
import tabula
import pdftotext

def extract_course_info(course):
    path = spec_to_get + ".pdf"
    filename = 'pdf_' + spec_to_get

    try:
        pdf_text = tabula.read_pdf(path, lattice=True, pandas_options={'header': None}, pages="all", multiple_tables=True)

        specification_data = {}

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


                for index, value in page.iloc[6].items():
                    if value == 'X':
                        if index == 1:
                            specification_data['Attendance Type'] = "Full Time"
                        elif index == 2:
                            specification_data['Attendance Type'] = "Part Time"

                for index, value in page.iloc[8].items():
                    if value == 'X':
                        if index == 1:
                            specification_data['Delivery Pattern'] = "Campus-based"
                        elif index == 2:
                            specification_data['Delivery Pattern'] = "Work-based"
                        elif index == 3:
                            specification_data['Delivery Pattern'] = "Online/distance"


        print(specification_data)
    except:
        print("Your PDF cannot be scraped.")

def web_scraping(course):
    return None



if __name__ == '__main__':
    scraping_method = input("Type in P for PDF scraper, W for Web Scraping, H for Help, or Q to Quit: ")
    if scraping_method == 'W':
        web_spec_to_get = input("Enter the website from which you want the course specification from: ")
        web_scraping(web_spec_to_get)
        print("To Do")
    elif scraping_method == 'P':
        spec_to_get = input("Enter in the course specification you would like to scrape: ")
        # ../ProgrammeSpecifications/BScComputerScience
        # ../ProgrammeSpecifications/BScDigitalDegreeApprenticeship
        extract_course_info(spec_to_get)
    elif scraping_method == 'H':
        print ("To Do")
    else:
        exit()