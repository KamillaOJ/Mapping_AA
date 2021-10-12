#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 12:00:57 2021

@author: kamilla
"""

###Find amino acid composition of the X in M2

M2 = {} 
M2keys = []
M2value = []
with open('/Users/Kamilla/documents/data/2M_redone/M2_correct.fasta', 'r') as f:
    for count, line in enumerate(f, start=0):
        if count % 2 == 0:
            M2keys.append(line[1:8])
        if count % 2 == 1:
            M2value.append(line[0:3])

M2 = dict(zip(M2keys, M2value))
lsequence = []
ssequence = ""

# Cath ID PH with M2
M2keys.sort()
print(M2keys)

# M2
for value in M2value:
    print(value)
    lsequence.append(value[1])

ssequence = "".join(lsequence)
print(lsequence)



AAs = ["A", "G", "E", "R", "W", "Y", "S", "N", "D", "C", "Q", "H", "I", "L",
        "K", "M", "F", "P", "T", "V"]

#sseqeunce written
sequence = "GGRKNHLQQLNRNRRPENNPSSNNNEVRKEESSTTTTNTGTQSSKKNMLEEGTFKSNNV"

totAA = len(sequence)/100
print(totAA)

for AA in AAs:
    AAcount = sequence.count(AA)
    percentage = AAcount/totAA
    print(F"{AA} = {AAcount} = {percentage:.2f}%")


hydrophobic = 0
aromatic = 0
positive = 0
negative = 0
non_polar = 0
polar = 0


for AA in AAs:
    AAcount = sequence.count(AA)
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
    AAcount = sequence.count(AA)
    percentage = AAcount/totAA
    print(AAcount)    
print("properties")
print(hydrophobic)
print(aromatic)
print(positive)
print(negative)
print(non_polar)
print(polar)





















