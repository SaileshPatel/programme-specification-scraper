import tabula

def extract_text(path):
    # pdf_text = tabula.read_pdf(path, lattice=True)
    # print(pdf_text) # print pandas.core.frame.DataFrame
    
    tabula.convert_into(path, 'pdf_tsv_file.tsv', 'tsv', lattice=True)
    tabula.convert_into(path, 'pdf_json_file.json', 'json', lattice=True)
    tabula.convert_into(path, 'pdf_csv_file.csv', lattice=True)

if __name__ == '__main__':
    extract_text('../ProgrammeSpecifications/BScComputerScience.pdf')