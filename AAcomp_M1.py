#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 11:13:59 2021

@author: kamilla
"""

#Motifs I think are correct from two rounds of FIMO and by looking at the 
#alignment. I think there are 26 motifs in 26 PH domains. 

AAs = ["A", "G", "E", "R", "W", "Y", "S", "N", "D", "C", "Q", "H", "I", "L",
       "K", "M", "F", "P", "T", "V"]

dmotifs = {"1eazA00": "KQGAVMKNWKRR", "1p6sA00": "KRGEYIKTWRPR",
          "1unqA00": "KRGEYIKTWRPR", "1wi1A01": "KNVWKRWKKR", 
          "1x05A00": "KQGHRRKNWKVR", "1x1gA00": "KQGHKRKNWKVR", 
          "1x1gA00": "KQGHKRKNWKVR", "2i5fA00": "KQGHRRKNWKVR", 
          "2x18E00": "KRGEYIKKNWRPR", "4gn1C02": "KDDGKKSWKKR", 
          "4kvgB02": "KEDGKKSWKRR", "1v5uA00": "KKGAFMKPWKAR", 
          "4khbB01": "KEPGKCR", "1faoA00": "KQGGLVKTWKTR", 
          "1fgyA00": "KLGGRVKTWKRR", "1fhwA00": "KLGGRVKTWKRR", 
          "1maiA00": "KVKSSSWRRER", "1u29A00": "KLGGGRVKTWKRR", 
          "2dhkA01": "KFGGKGPIRGWKSR", "3ml4C01": "KLRDGKKWKSR", 
          "3mpxA02": "KVTGKNRRPR", "1tqzA01": "RIPPRASNRGYRASDWKLDQPDWTGRLR", 
          "1xkeA00": "RFDAEVSQWKER", "4hatB00": "RFDKDAKEWKER", 
          "416eA00": "RWDRDVSQWKER", "5cllB00": "RFDVESKEWKER", 
          "2dkpA01": "KQDSTGMKLWKKR"}

#Full motif 320 AAs total
pdbs = []
lmotifs = []
smotifs = ""

#motif -2 26 AA total
l_min2 = []
s_min2 = ""

#motif Xn 216 AAs total
l_Xn = []
s_Xn = ""

for key in dmotifs:
    pdbs.append(key)
    lmotifs.append(dmotifs[key])

for seq in lmotifs:
    l_min2.append(seq[-2])
    l_Xn.append(seq[1:-3])

smotifs = "".join(lmotifs)
s_min2 = "".join(l_min2)
s_Xn = "".join(l_Xn)

for motif in lmotifs:
    print(len(motif))




# Find how many amino acids in the motif
AAtot = 2.16
for AA in AAs:
    AAcount = s_Xn.count(AA)
    percentage = AAcount/AAtot
    print(F"{AA} = {AAcount} = {percentage:.2f}%")
 
hydrophobic = 0
aromatic = 0
positive = 0
negative = 0
non_polar = 0
polar = 0    
 
for AA in AAs:
    AAcount = s_Xn.count(AA)
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
                
hp = hydrophobic/AAtot           
ap = aromatic/AAtot 
ppos = positive/AAtot
np = negative/AAtot       
npp = non_polar/AAtot
ppol = polar/AAtot      
        
print(f"Hydrophobic AAs = {hydrophobic} = {hp:.2f}%")
print(f"Aromatic AAs = {aromatic} = {ap:.2f}%")
print(f"Positive AAs = {positive} = {ppos:.2f}%")
print(f"Negative AAs = {negative} = {np:.2f}%")
print(f"Non polar AAs = {non_polar} = {npp:.2f}%")
print(f"Polar AAs = {polar} = {ppol:.2f}%")


"""for easier adding to excel"""
for AA in AAs:
    AAcount = s_Xn.count(AA)
    percentage = AAcount/AAtot
    print(AAcount)    
print("properties")
print(hydrophobic)
print(aromatic)
print(positive)
print(negative)
print(non_polar)
print(polar)