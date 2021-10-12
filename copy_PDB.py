#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 11:04:49 2021

@author: kamilla
"""
import os
import shutil

###copy all PDB files corresponding to the CATH id stored in a list into a now folder

F21 = ['2pz1A03', '1w1hD00', '5d3xB00', '4chjA00', '2yf0A01', '3au4A04',
       '2d9vA01', '2i1jA03', '4yl8A03', '3hk0B02', '1kz7C02', '2cofA00',
       '1foeC02', '3syxA00', '2vrwB02', '2lulA00', '2dhiA00', '2kcjA00',
       '1mkeA00', '3f0wA00', '3zvrA03']

# M59_2 = ["1btnA00", "1ddvA00", "1ddwA00", "1droA00", "1v5uA00", "2d9yA00",
#          "2da0A00", "2yryA00", "3tfmA02", "1dynA00", "1v89A00", "2dhiA00",
#          "1eazA00", "1wgqA00", "2dhkA01", "2ys3A00", "1egxA00", "1wi1A01",
#          "2dkpA01", "3a8pB01", "4f7hA00", "1faoA00", "1wjmA00", "2dn6A00",
#          "3aj4A00", "4gn1C02", "1fgyA00", "1x05A00", "2i5fA00", "4hatB00",
#          "1fhwA00", "1x1fA00", "2p0hA00", "3hk0B02", "4k2pD01", "1p6sA00",
#          "1x1gA00", "2p8vA00", "3ml4C01", "4k81A02", "1qc6A00", "2codA01", 
#          "2q13A02", "3oanA00", "4kvgB02", "1u29A00", "2cy5A00", "2rloA00",
#          "3pp2A00", "4wsfA00", "1unqA00", "2d9vA01", "2vszB02", "3qbvB02",
#          "5cllB00", "1upqA00", "2d9wA01", "2x18E00", "5l81B00"]

def motifpdbs():
    os.mkdir("F21_raw")

    for pdb in F21:
        shutil.copy(f"/Users/Kamilla/documents/data/all_PH_raw/{pdb}.pdb", f"F21_raw/{pdb}.pdb")

motifpdbs()
