#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 09:06:21 2021

@author: kamilla
"""

###Find the amino acid sequences from all PDB files in a folder,
### and save it to a fasta file

import sys


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


        #seq_file.write(f">{filename_pdb[11:18]}\n")
        #seq_file.write(new_sequence)
        #seq_file.write("\n")

        seq_file.write(f"{filename_pdb[11:18]}\n")


#in all_PH_raw:
for file in sys.argv[3:]:
    if str(file[11:18]) in cath_S:
        find_sequence(file, sys.argv[2])
        
###what i wrote in the command line for S100:
###data kamilla$ python FS_all_PH.py cath_S100.txt all_PH_S100.fasta all_PH_raw/*.pdb

###what i wrote in the command line for S95:
###data kamilla$ python FS_all_PH.py cath_S95.txt all_PH_S95.fasta all_PH_raw/*.pdb

###what i wrote in the command line for S160:
###data kamilla$ python FS_all_PH.py cath_S60.txt all_PH_S60.fasta all_PH_raw/*.pdb

###what i wrote in the command line for S35:
###data kamilla$ python FS_all_PH.py cath_S35.txt all_PH_S35.fasta all_PH_raw/*.pdb
        
