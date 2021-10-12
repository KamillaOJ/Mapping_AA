import sys

with open("/Users/Kamilla/documents/data/fake_PH.csv", "r") as fake_PH:
    lfake_PH = fake_PH.readlines()
    IDfake_PH = []
    for ID in lfake_PH:
        IDfake_PH.append(ID.strip())

with open (sys.argv[1], "r") as cath:
    cath_S = []
    lines = cath.readlines()
    for line in lines:
        cath_S.append(line[0:7])

def find_template(filename_pdb, filename_txt):
    with open(filename_pdb, "r") as pdb_file, open(filename_txt, "a") as temp_file:
        temp_file.write(f">{filename_pdb[11:18]}  _P_ {filename_pdb[11:16]}\n")


for file in sys.argv[3:]:
    if str(file[11:18]) in cath_S and str(file[11:18]) not in IDfake_PH:
        find_template(file, sys.argv[2])




###what i wrote in the command line for S60:
###data kamilla$ python realPH_S60_template_TcofAdv.py cath_S60.txt NF_PH_temp_S60.txt all_PH_raw/*.pdb
