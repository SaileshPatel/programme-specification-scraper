# course-programme-specification-scraper

A programme written by Sailesh Patel (160034811) designed to scrape information from course programme specification PDFs, as a part of the FYP project, A Chatbot for Assisting University Admission Process, supervised by Dr Sylvia Wong. 

## Tech Used
* [Tabula-Py] (https://tabula-py.readthedocs.io/en/latest/getting_started.html#installation)
* [BeautifulSoup] (https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup)
* [Requests] (https://requests.readthedocs.io/en/master/user/install/)
* Python 3.7.7
* pip 20.0.2 

## Installation
1. Clone the repository
2. Install the required technologies listed above (**Note** PIP is not required, but would be beneficial to install Tabula-Py and BeautifulSoup)

## Usage
* Use the command `python programme-scraper.py` to execute the scraper
* Select the option you want to use (P for PDF scraping, W for Website Scraping)
* If you select P, type in file location of the PDF file (without the PDF extension) relative to where the script is located
* If you select W, type 'EAS' for the school and type in https://www2.aston.ac.uk/study/courses/computer-science-bsc for the website

## License
All Rights Reserved