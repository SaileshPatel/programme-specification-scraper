# course-programme-specification-scraper

A programme written by Sailesh Patel (160034811) designed to scrape information from course programme specification PDFs, as a part of the FYP project, A Chatbot for Assisting University Admission Process, supervised by Dr Sylvia Wong. 

## Tech Used
* [Tabula-Py](https://tabula-py.readthedocs.io/en/latest/getting_started.html#installation)
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup)
* [Requests](https://requests.readthedocs.io/en/master/user/install/)
* [Python 3.7.7](https://www.python.org/downloads/release/python-377/)
* [pip 20.0.2](https://pip.pypa.io/en/stable/installing/)  

## Installation
1. Clone the repository
2. Install the required technologies listed above (the links are to their respective installation instructions)


**Note** PIP is not required, but would be beneficial to install Tabula-Py, BeautifulSoup, and Requests

## Usage
* Please ensure that all the software requirements have been met before executing the program
* To execute the program, run the command python3 programme-scraper.py
* To run the PDF scraper
    * Type ‘P’ and press ‘Enter’
	* Type the PDF file in without the ‘.pdf’ extension and press ‘Enter’
        * BScComputerScience shows the PDF scraper working
        * BScDigitalDegreeApprenticeship shows the PDF scraper not working
* To run the web scraper
    * Type ‘W’ and press ‘Enter’
        * Type ‘EAS’ for the school and press ‘Enter’
        * Type the website you would like to scrape
            * Type ‘https://www2.aston.ac.uk/study/courses/computer-science-bsc’ to show the web scraper working
            * Type ‘https://www2.aston.ac.uk/study/courses/chemistry-bsc’ to show the web scraper fail to format the text inside the Entry Requirements & Fees for 2020



## License
All Rights Reserved