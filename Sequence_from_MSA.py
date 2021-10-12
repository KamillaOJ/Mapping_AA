#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 11:42:02 2021

@author: kamilla
"""

### Cut an MSA and save the sequence from the excerpt as a fasta file

import sys
from Bio import AlignIO


def findexcerptseq(filename_txt):
    with open(filename_txt, "a") as seq_file:
        alignmentfile = "/Users/Kamilla/documents/data/PROMALS3D_aln/P3D_S95_aln.fa"
        alignment = AlignIO.read(alignmentfile, "fasta")

        excerpt_range = [135,160]

        seqresults_excerpt = {}
        lenresults_excerpt = {}

        for record in alignment:
            seqid = record.id[:7]
            seq = record.seq
            excerpt_stripped = seq[excerpt_range[0]:excerpt_range[1]]
            excerpt_ungapped = excerpt_stripped.ungap()
            sequence = str(excerpt_ungapped)
            excerpt_len = len(excerpt_ungapped)

            seqresults_excerpt[seqid] = excerpt_ungapped
            lenresults_excerpt[seqid] = excerpt_len

            seq_file.write(f">{seqid}\n")
            seq_file.write(sequence)
            seq_file.write("\n")

        # print(seqresults_b1loop1b2)
        # print(lenresults_b1loop1b2)


findexcerptseq(sys.argv[1])




### Used to test the script throughout writing it
# alignmentfile = "/Users/Kamilla/documents/data/PROMALS3D_aln/56motif.fa"
# alignment = AlignIO.read(alignmentfile, "fasta")

# b1loop1b2_range = [50,130]

# seqresults_b1loop1b2 = {}
# lenresults_b1loop1b2 = {}

# for record in alignment:
#     seqid = record.id[:7]
#     seq = record.seq
#     loop_stripped = seq[b1loop1b2_range[0]:b1loop1b2_range[1]]
#     loop_ungapped = loop_stripped.ungap()
#     loop_len = len(loop_ungapped)

#     seqresults_b1loop1b2[seqid] = loop_ungapped
#     lenresults_b1loop1b2[seqid] = loop_len
