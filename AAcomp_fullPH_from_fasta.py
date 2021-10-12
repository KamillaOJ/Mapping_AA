#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  3 11:18:11 2021

@author: kamilla
"""

### Finding the amino acid composition of a full domain from fasta file

AAs = ["A", "G", "E", "R", "W", "Y", "S", "N", "D", "C", "Q", "H", "I", "L",
       "K", "M", "F", "P", "T", "V"]


#Open the sequence file and save the content as a single string
with open ("/Users/Kamilla/documents/data/Motif/M1and2_noID.fasta", "r") as seqfile:
    sequences = seqfile.read()

#Get the number of AAs in the sequences, 18614 AA total
#print(len(sequences))

totAA = len(sequences)/100
print(totAA)

for AA in AAs:
    AAcount = sequences.count(AA)
    percentage = AAcount/totAA
    print(F"{AA} = {AAcount} = {percentage:.2f}%")
    

hydrophobic = 0
aromatic = 0
positive = 0
negative = 0
non_polar = 0
polar = 0


for AA in AAs:
    AAcount = sequences.count(AA)
    if AA == "L":
        hydrophobic = hydrophobic + AAcount
    elif AA == "I":
        hydrophobic = hydrophobic + AAcount
    elif AA == "C":
        hydrophobic = hydrophobic + AAcount
    elif AA == "M":
        hydrophobic = hydrophobic + AAcount
    elif AA == "W":
        hydrophobic = hydrophobic + AAcount 
        aromatic = aromatic + AAcount
    elif AA == "Y":
        hydrophobic = hydrophobic + AAcount
        aromatic = aromatic + AAcount
    elif AA == "F":
        hydrophobic = hydrophobic + AAcount
        aromatic = aromatic + AAcount
    elif AA == "D":
        negative = negative + AAcount
    elif AA == "E":
        negative = negative + AAcount
    elif AA == "V":
        non_polar = non_polar + AAcount
    elif AA == "A":
        non_polar = non_polar + AAcount
    elif AA == "G":
        non_polar = non_polar + AAcount
    elif AA == "P":
        non_polar = non_polar + AAcount
    elif AA == "S":
        polar = polar + AAcount
    elif AA == "N":
        polar = polar + AAcount
    elif AA == "Q":
        polar = polar + AAcount
    elif AA == "T":
        polar = polar + AAcount
    elif AA == "H":
        positive = positive + AAcount
    elif AA == "K":
        positive = positive + AAcount        
    elif AA == "R":
        positive = positive + AAcount
        
        
hp = hydrophobic/totAA           
ap = aromatic/totAA 
ppos = positive/totAA
np = negative/totAA       
npp = non_polar/totAA 
ppol = polar/totAA       
        


print(f"Hydrophobic AAs = {hydrophobic} = {hp:.2f}%")
print(f"Aromatic AAs = {aromatic} = {ap:.2f}%")
print(f"Positive AAs = {positive} = {ppos:.2f}%")
print(f"Negative AAs = {negative} = {np:.2f}%")
print(f"Non polar AAs = {non_polar} = {npp:.2f}%")
print(f"Polar AAs = {polar} = {ppol:.2f}%")

"""for easier adding to excel"""

for AA in AAs:
    AAcount = sequences.count(AA)
    percentage = AAcount/totAA
    print(AAcount)    
print("properties")
print(hydrophobic)
print(aromatic)
print(positive)
print(negative)
print(non_polar)
print(polar)



