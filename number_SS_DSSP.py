#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 19:37:07 2021

@author: kamilla
""" 
"""Finding the number of secondary structures in each PH domain in the 
datasets used in my master project "Mapping the amino acid composition in the
 IBS of PH domains" """

import sys


def find_number_Bstrands (pdb_file, output_file):
    from Bio.PDB import PDBParser
    from Bio.PDB.DSSP import DSSP
    p = PDBParser()
    #cath_id = (f"{pdb_file[0, 7]}")
    structure = p.get_structure("id", pdb_file)
    model = structure [0]
    mkdssp = DSSP(model, pdb_file, dssp='mkdssp')


    SS = 0
    SS_string = ""


    length = (len(list(mkdssp.keys())))
    for n in range (length):
        a_key = (mkdssp.keys()[n]) ### The number gives the AA in this number
        prev_key = (mkdssp.keys()[n-1])
        #print(mkdssp[a_key][2]) ### 2 shows only the secondary structure. H = Helix, E = strand

        if mkdssp[a_key][2] == "E" and mkdssp[prev_key][2] != "E":
            SS = SS + 1
    SS_string = str(SS)


    with open(output_file, "a") as output:
            output.write(SS_string)
            output.write("\n")

def find_id(pdb_file, output_file):
    with open(output_file, "a") as output:
        output.write(f"{pdb_file[9:16]}\n")

for file in sys.argv[2:]:
    find_number_Bstrands(file, sys.argv[1])

for file in sys.argv[2:]:
    find_id(file, sys.argv[1])

### Write in terminal:
###data kamilla$ python dssp.py 1M26_Bstrands.txt 26motif_pdbs_raw/*.pdb

def find_number_Ahelices (pdb_file, output_file):
    from Bio.PDB import PDBParser
    from Bio.PDB.DSSP import DSSP
    p = PDBParser()
    #cath_id = (f"{pdb_file[0, 7]}")
    structure = p.get_structure("id", pdb_file)
    model = structure [0]
    mkdssp = DSSP(model, pdb_file, dssp='mkdssp')


    SS = 0
    SS_string = ""


    length = (len(list(mkdssp.keys())))
    for n in range (length):
        a_key = (mkdssp.keys()[n]) ### The number gives the AA in this number
        prev_key = (mkdssp.keys()[n-1])
        #print(mkdssp[a_key][2]) ### 2 shows only the secondary structure. H = Helix, E = strand

        if mkdssp[a_key][2] == "H" and mkdssp[prev_key][2] != "H":
            SS = SS + 1
    SS_string = str(SS)


    with open(output_file, "a") as output:
            output.write(SS_string)
            output.write("\n")

def find_id(pdb_file, output_file):
    with open(output_file, "a") as output:
        output.write(f"{pdb_file[9:16]}\n")

for file in sys.argv[2:]:
    find_number_Ahelices(file, sys.argv[1])

for file in sys.argv[2:]:
    find_id(file, sys.argv[1])


### Write in terminal:
###data kamilla$ python dssp.py 1M26_ahelices.txt 26motif_pdbs_raw/*.pdb





""""Test, that worked"""
### Used to test the script while writing it

# from Bio.PDB import PDBParser
# from Bio.PDB.DSSP import DSSP
# p = PDBParser()
# structure = p.get_structure("1fgyA00", "/Users/Kamilla/documents/data/Motif/26motif_pdbs_raw/1fgyA00.pdb")
# model = structure [0]
# mkdssp = DSSP(model, '/Users/Kamilla/documents/data/Motif/26motif_pdbs_raw/1fgyA00.pdb', dssp='mkdssp')


# SS = 0
# nbSS = []
# b_strands = {}

# length = (len(list(mkdssp.keys())))
# for n in range (length):
#     a_key = (mkdssp.keys()[n])### The number gives the AA in this number
#     prev_key = (mkdssp.keys()[n-1])
#     #print(mkdssp[a_key][2]) ### 2 shows only the secondary structure. H = Helix, E = strand

#     if mkdssp[a_key][2] == "E" and mkdssp[prev_key][2] != "E":
#         SS = SS + 1

#     b_strands[structure] = SS
