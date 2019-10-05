import tabula

def extract_text(path):
    pdf_text = tabula.read_pdf(path)
    print(pdf_text) # print pandas.core.frame.DataFrame

if __name__ == '__main__':
    extract_text('../ProgrammeSpecifications/BScComputerScience.pdf')
