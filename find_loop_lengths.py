#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 15:26:47 2021

@author: kamilla
"""

from Bio import AlignIO



alignmentfile = "/Users/Kamilla/documents/data/Motif/26motifPROMALS3D.aln"
alignment = AlignIO.read(alignmentfile, "clustal")

#Mloop_range = [284, 302]
loop1_range = [50, 70]
loop2_range = [95, 108]
loop3_range = [123, 142]


seqresults_loop1 = {}
lenresults_loop1 = {}
lseqloop1 = []
sseqloop1 = ""

seqresults_loop2 = {}
lenresults_loop2 = {}
lseqloop2 = []
sseqloop2 = ""

seqresults_loop3 = {}
lenresults_loop3 = {}
lseqloop3 = []
sseqloop3 = ""


seqresults = {}
lenresults = {}
lseq = []
sseq = ""

# seqresults_Mloop = {}
# lenresults_Mloop = {}
# lseqMloop = []
# sseqMloop = ""



"""Finding the loop lengths"""
for record in alignment:
    seqid = record.id[:7]
    seq = record.seq

    #Loop 1
    loop_stripped1 = seq[loop1_range[0]:loop1_range[1]]
    loop_ungapped1 = loop_stripped1.ungap()
    sequence1 = str(loop_ungapped1)
    loop_len1 = len(loop_ungapped1)

    seqresults_loop1[seqid] = loop_ungapped1
    lenresults_loop1[seqid] = loop_len1

    lseqloop1.append(sequence1)
    sseqloop1 = "".join(lseqloop1)

    # Loop 2
    loop_stripped2 = seq[loop2_range[0]:loop2_range[1]]
    loop_ungapped2 = loop_stripped2.ungap()
    sequence2 = str(loop_ungapped2)
    loop_len2 = len(loop_ungapped2)

    seqresults_loop2[seqid] = loop_ungapped2
    lenresults_loop2[seqid] = loop_len2

    lseqloop2.append(sequence2)
    sseqloop2 = "".join(lseqloop2)

#Loop 3
    loop_stripped3 = seq[loop3_range[0]:loop3_range[1]]
    loop_ungapped3 = loop_stripped3.ungap()
    sequence3 = str(loop_ungapped3)
    loop_len3 = len(loop_ungapped3)

    seqresults_loop3[seqid] = loop_ungapped3
    lenresults_loop3[seqid] = loop_len3

    lseqloop3.append(sequence3)
    sseqloop3 = "".join(lseqloop3)

print("Lenghts for Loop 1:")
for lenght in lseqloop1:
    print(len(lenght))
print("\n")

print("Lenghts for Loop 2:")
for lenght in lseqloop2:
    print(len(lenght))
print("\n")

print("Lenghts for Loop 3:")
for lenght in lseqloop3:
    print(len(lenght))
