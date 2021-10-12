#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 19 13:15:12 2021

@author: kamilla
"""
import sys

### Find all the sequences in CATH S60 who are confirmed PH domains 
### and store their sequences in a fasta file. Then count the sequences

with open("/Users/Kamilla/documents/data/fake_PH.csv", "r") as fake_PH:
    lfake_PH = fake_PH.readlines()
    IDfake_PH = []
    for ID in lfake_PH:
        IDfake_PH.append(ID.strip())

#print(IDfake_PH)



with open (sys.argv[1], "r") as cath:
    cath_S = []
    lines = cath.readlines()
    for line in lines:
        cath_S.append(line[0:7])


def find_sequence(filename_pdb, filename_txt):
    """Get the AA sequence from a PDB file and save it in a text file"""
    with open(filename_pdb, "r") as pdb_file, open(filename_txt, "a") as seq_file:
        ca_lines = []
        sequence = ""
        lines = pdb_file.readlines()

        amino_acids = {"ALA": "A", "GLY": "G", "GLU": "E", "ARG": "R",
                "TRP": "W", "TYR": "Y", "SER": "S", "ASN": "N",
                "ASP": "D", "CYS": "C", "GLN": "Q", "HIS": "H",
                "ILE": "I", "LEU": "L", "LYS": "K", "MET": "M",
                "PHE": "F", "PRO": "P", "THR": "T", "VAL": "V"}

        for line in lines:
            if line[12:16].strip() == "CA":
                ca_lines.append(line)
                sequence = sequence + amino_acids[line[17:20]]

        new_sequence = ""
        for aa in sequence:
            new_sequence += aa
            if len(new_sequence.replace("\n", "")) % 70 == 0:
                new_sequence += "\n"


        seq_file.write(f">{filename_pdb[11:18]}\n")
        seq_file.write(new_sequence)
        seq_file.write("\n")


for file in sys.argv[3:]:
    if str(file[11:18]) in cath_S and str(file[11:18]) not in IDfake_PH:
        find_sequence(file, sys.argv[2])

with open(sys.argv[2], "r") as file:
    data = file.read()
    pdb_number = data.count(">")
    print(f"The number of PDBs in {sys.argv[2]} is {pdb_number}")



###what i wrote in the command line for S60:
###data kamilla$ python find_realPH_S60_seqs.py cath_S60.txt NF_all_PH_S60.fasta all_PH_raw/*.pdb
