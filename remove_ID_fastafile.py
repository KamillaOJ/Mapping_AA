#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 14:20:26 2021

@author: kamilla
"""

### Remove name/id from fastafile, and join all sequences
def find_sequence(fastafile, filename_txt):
    with open(fastafile, "r") as FF, open(filename_txt, "a") as seq_file:
        lines = FF.readlines()
        ssequence = ""
        lsequence = []
        lsequence_stripped = []
        
        for line in lines:
            if line[0] != ">":
                lsequence.append(line)
        
        for seq in lsequence:
            lsequence_stripped.append(seq.strip())
        
        ssequence = "".join(lsequence_stripped)
        
        
        seq_file.write(ssequence)
        
        


find_sequence("/Users/Kamilla/documents/data/Motif/M1and2.fasta", "M1and2_noID.fasta")

"""Test to see if the file is ok"""
# with open("/Users/Kamilla/documents/data/Motif/M1and2.fasta") as seq_file:
#     print(seq_file.readlines())