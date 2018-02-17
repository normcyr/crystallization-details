import pypdb
import get_crystallization_exp as xtal_exp

# create the list of PDB codes from the text file
pdb_code_list = []
with open('pdb_code_list.txt', 'r') as f:
    for pdb_code in f:
        # strip the linebreak character present at the end of each line
        pdb_code_list.append(pdb_code.strip())

# verify if it is a X-ray diffraction structure
for pdb_code in pdb_code_list:

    # get the description
    pdb_dict = pypdb.describe_pdb(pdb_code)

    # look for the experimental method
    if pdb_dict['expMethod'] == 'X-RAY DIFFRACTION':
            crystallization_details = xtal_exp.get_info(pdb_code)
            print(crystallization_details)
