#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 11:25:28 2021

@author: kamilla
"""


import sys
from Bio import AlignIO


alignmentfile = "/Users/Kamilla/documents/data/PROMALS3D_aln/56motif.fa"
alignment = AlignIO.read(alignmentfile, "fasta")

b1loop1b2_range = [50,130]

seqresults_b1loop1b2 = {}
lenresults_b1loop1b2 = {}

for record in alignment:
    seqid = record.id[:7]
    seq = record.seq
    loop_stripped = seq[b1loop1b2_range[0]:b1loop1b2_range[1]]
    loop_ungapped = loop_stripped.ungap()
    loop_len = len(loop_ungapped)

    seqresults_b1loop1b2[seqid] = loop_ungapped
    lenresults_b1loop1b2[seqid] = loop_len

def findloopseq(filename_txt):
    with open(filename_txt, "a") as seq_file:
        alignmentfile = "/Users/Kamilla/documents/data/PROMALS3D_aln/56motif.fa"
        alignment = AlignIO.read(alignmentfile, "fasta")

        b1loop1b2_range = [50,130]

        seqresults_b1loop1b2 = {}
        lenresults_b1loop1b2 = {}

        for record in alignment:
            seqid = record.id[:7]
            seq = record.seq
            loop_stripped = seq[b1loop1b2_range[0]:b1loop1b2_range[1]]
            loop_ungapped = loop_stripped.ungap()
            sequence = str(loop_ungapped)
            loop_len = len(loop_ungapped)

            seqresults_b1loop1b2[seqid] = loop_ungapped
            lenresults_b1loop1b2[seqid] = loop_len

            seq_file.write(f">{seqid}\n")
            seq_file.write(sequence)
            seq_file.write("\n")

        # print(seqresults_b1loop1b2)
        # print(lenresults_b1loop1b2)


findloopseq(sys.argv[1])
