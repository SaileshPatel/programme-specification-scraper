import tabula

def extract_text(path):
    pdf_text = tabula.read_pdf(path)
    print(pdf_text) # print pandas.core.frame.DataFrame

    tabula.convert_into(path, 'pdf_tsv_file.tsv', 'tsv')
    tabula.convert_into(path, 'pdf_json_file.json', 'json')
    tabula.convert_into(path, 'pdf_csv_file.csv')

if __name__ == '__main__':
    extract_text('../ProgrammeSpecifications/BScComputerScience.pdf')