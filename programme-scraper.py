import pandas as pd
import tabula
import requests
from bs4 import BeautifulSoup

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
    except Exception as ex:
        print("Your PDF cannot be scraped.")
        print(ex)

def web_scraping(school, course):
    try:
        res = requests.get(course)
        soup = BeautifulSoup(res.content, 'lxml')
        course_info = {}
        database_info = {}

        if school == 'ABS' :
            return None
        elif school == 'AMS' :
            return None
        elif school == 'EAS' :
            #['Career Prospects', 'Entry Requirements & Fees for 2020', 'Course Outline & Modules', 'Placement Year', 'Learning, Teaching & Assessment', 'Teaching Staff', 'Contact Us']
            for info_accordion in soup.find_all("div", {"class": "accordion"}):
                itemName = "" # temporary storage for name of the key
                for title in info_accordion.find_all("a", {"class": "accordion__title"}):
                    itemName = title.text
                    course_info[itemName] = ""
                for info in info_accordion.find_all("div", {"class": "accordion__inner"}):
                    course_info[itemName] = info.text.strip().replace('\n', ' ').encode("ascii", "ignore")
        elif school == 'LHS' :
            return None
        elif school == 'LSS':
            return None
        else: 
            print("invalid school choice")
        print(course_info)
    except Exception as ex:
        print("The URL you have provided cannot be scraped.")
        print(ex)

if __name__ == '__main__':
    scraping_method = input("Type in P for PDF scraper, W for Web Scraping, H for Help, or Q to Quit: ")
    if scraping_method == 'W':
        # https://www2.aston.ac.uk/study/courses/computer-science-bsc
        course_school = input("Enter the school which the course you want to scrape belongs to:\nABS - Aston Business School\nAMS - Aston Medical School\nEAS - Engineering & Applied Sciences\nLHS - Life & Health Sciences\nLSS - Languages & Social Sciences\n")
        web_spec_to_get = input("Enter the website from which you want the course specification from: ")
        web_scraping(course_school, web_spec_to_get)
    elif scraping_method == 'P':
        spec_to_get = input("Enter in the course specification you would like to scrape: ")
        # ../ProgrammeSpecifications/BScComputerScience
        # ../ProgrammeSpecifications/BScDigitalDegreeApprenticeship
        extract_course_info(spec_to_get)
    elif scraping_method == 'H':
        print ("To Do")
    else:
        exit()