import sys
import os
import shutil

with open (sys.argv[1], "r") as cath:
    cath_S = []
    lines = cath.readlines()
    for line in lines:
        cath_S.append(line[0:7])

def motifpdbs():
    os.mkdir(sys.argv[2])
    shutil.copy(f"/Users/Kamilla/documents/data/all_PH_raw/{pdb}.pdb", f"sys.argv[2]/{pdb}.pdb")

for pdb in sys.argv[3:]:
    if str(file[10:17]) in cath_S:



motifpdbs()
