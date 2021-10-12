#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 19 18:25:19 2021

@author: kamilla
"""

### Script used to find conserved AAs at specific positions reletive to structure

from Bio import AlignIO

alignmentfile = "/Users/Kamilla/documents/data/NCAS95_59Tcof.aln"
#alignmentfile = "/Users/Kamilla/documents/data/NF_S60_P3D.aln"
alignment = AlignIO.read(alignmentfile, "clustal")

w_range = [138, 141]

seqresults_w = {}
lenresults_w = {}
lseqw = []
for record in alignment:
    seqid = record.id[:7]
    seq = record.seq
    w_stripped = seq[w_range[0]:w_range[1]]
    w_ungapped = w_stripped.ungap()
    sequence = str(w_ungapped)
    w_len = len(w_ungapped)

    seqresults_w[seqid] = w_ungapped
    lenresults_w[seqid] = w_len

    lseqw.append(sequence)
    sseqw = "".join(lseqw)

w = 0
f = 0
y = 0
k = 0
r = 0
l = 0
g = 0
k_r = 0
y_f = 0
w_y = 0
w_f = 0
 

   
#print(sseqw.count("Y"))
for seq in lseqw:
    # if "W" in seq:
    #     w = w + 1
    # if "F" in seq:
    #     f = f + 1
    # if "Y" in seq:
    #     y = y + 1
    if "K" in seq and "R" in seq:
        k_r = k_r + 1
    #if "W"  in seq and "Y" in seq:
        #w_y = w_y + 1
    # if "Y"  in seq:
    #     y = y + 1
    # if "F"  in seq:
    #     f = f + 1
    if "R" in seq:
        r = r + 1
    if "K" in seq:
        k = k + 1
    # if "G" in seq:
    #     g = g + 1
print(f"R = {r}")        
print(f"K = {k}")        
#print(f"Y and F = {y_f}")
print(f"K and R = {k_r}")
#print(f"W and Y = {w_y+2}")

#print(f"W = {w}, F = {f}, Y = {y}")

# Only counting one per seq
# 47W, 10F, 7Y from [103, 107]

# Find how many amino acids in the motif

AAs = ["A", "G", "E", "R", "W", "Y", "S", "N", "D", "C", "Q", "H", "I", "L",
       "K", "M", "F", "P", "T", "V"]

# AAtot = 1.66
# for AA in AAs:
#     AAcount = sseqloop.count(AA)
#     percentage = AAcount/AAtot
#     print(F"{AA} = {AAcount} = {percentage:.2f}%")