#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 15:57:32 2021

@author: kamilla
"""

###Overview of the datasets concerning binding motifs and datasets of non-PH domains
###code for finding out which domains are non-PH domains





"""Motif Datasets"""

F56 =  ['3ml4C01', '2x18E00', '1eazA00', '1p6sA00', '1unqA00', '2i5fA00',
        '1x1gA00', '1x05A00', '1wi1A01', '1fhwA00', '1u29A00', '1fgyA00',
        '1faoA00', '1v5uA00', '4kvgB02', '4hatB00', '5cllB00', '4gn1C02',
        '2dkpA01', '3mpxA02', '4khbB01', '2pz1A03', '1w1hD00', '1v89A00',
        '3voqA00', '1maiA00', '5l81B00', '2ys3A00', '2dhkA01', '5d3xB00',
        '2crfA01', '1tqzA01', '4chjA00', '2yf0A01', '3au4A04',
        '1xkeA00', '1p3rC00', '2d9zA01', '2d9vA01', '2i1jA03', '4yl8A03',
        '2d9wA01', '4l6eA00', '3hk0B02', '1kz7C02', '2cofA00', '1foeC02',
        '3syxA00', '3tfmA02', '2vrwB02', '2lulA00', '2dhiA00', '2kcjA00',
        '1mkeA00', '3f0wA00', '3zvrA03']

F35 = ["1eazA00", "1tqzA01", "1x1gA00", "2i5fA00", "4gn1C02", "1faoA00",
       "1u29A00", "1xkeA00", "2x18E00", "4hatB00", "1fgyA00", "1unqA00",
       "2crfA01", "2ys3A00", "4khbB01", "1fhwA00", "1v5uA00", "2d9wA01",
       "3ml4C01", "4kvgB02", "1maiA00", "1v89A00", "2d9zA01", "3mpxA02", 
       "4l6eA00", "1p3rC00", "1wi1A01", "2dhkA01", "3tfmA02", "5cllB00",
       "1p6sA00", "1x05A00", "2dkpA01", "3voqA00", "5l81B00"] 

M26_1 = ["1eazA00", "1tqzA01", "1x1gA00", "3ml4C01", "4l6eA00", "1faoA00",
        "1u29A00", "1xkeA00", "3mpxA02", "5cllB00", "1fgyA00", "1unqA00",
        "2dhkA01", "4gn1C02", "1fhwA00", "1v5uA00", "2dkpA01", "4hatB00", 
        "1maiA00", "1wi1A01", "2i5fA00", "4khbB01", "1p6sA00", "1x05A00",
        "2x18E00", "4kvgB02"]

M59_2 = ["1btnA00", "1ddvA00", "1ddwA00", "1droA00", "1v5uA00", "2d9yA00",
         "2da0A00", "2yryA00", "3tfmA02", "1dynA00", "1v89A00", "2dhiA00",
         "1eazA00", "1wgqA00", "2dhkA01", "2ys3A00", "1egxA00", "1wi1A01",
         "2dkpA01", "3a8pB01", "4f7hA00", "1faoA00", "1wjmA00", "2dn6A00",
         "3aj4A00", "4gn1C02", "1fgyA00", "1x05A00", "2i5fA00", "4hatB00",
         "1fhwA00", "1x1fA00", "2p0hA00", "3hk0B02", "4k2pD01", "1p6sA00",
         "1x1gA00", "2p8vA00", "3ml4C01", "4k81A02", "1qc6A00", "2codA01", 
         "2q13A02", "3oanA00", "4kvgB02", "1u29A00", "2cy5A00", "2rloA00",
         "3pp2A00", "4wsfA00", "1unqA00", "2d9vA01", "2vszB02", "3qbvB02",
         "5cllB00", "1upqA00", "2d9wA01", "2x18E00", "5l81B00"]

M1and2 = ['1eazA00', '1x1gA00', '3ml4C01', '1faoA00', '1u29A00', '5cllB00',
          '1fgyA00', '1unqA00', '2dhkA01', '4gn1C02', '1fhwA00', '1v5uA00', 
          '2dkpA01', '4hatB00', '1wi1A01', '2i5fA00', '1p6sA00', '1x05A00',
          '2x18E00', '4kvgB02']

OM1 = ['1tqzA01', '4l6eA00', '1xkeA00', '3mpxA02', '1maiA00', '4khbB01']

OM2 = ['1btnA00', '1ddvA00', '1ddwA00', '1droA00', '2d9yA00', '2da0A00',
       '2yryA00', '3tfmA02', '1dynA00', '1v89A00', '2dhiA00', '1wgqA00',
       '2ys3A00', '1egxA00', '3a8pB01', '4f7hA00', '1wjmA00', '2dn6A00',
       '3aj4A00', '1x1fA00', '2p0hA00', '3hk0B02', '4k2pD01', '2p8vA00',
       '4k81A02', '1qc6A00', '2codA01', '2q13A02', '3oanA00', '2cy5A00',
       '2rloA00', '3pp2A00', '4wsfA00', '2d9vA01', '2vszB02', '3qbvB02',
       '1upqA00', '2d9wA01', '5l81B00']

"""Fake PH datasets"""
FakeS95 = ['1ntvA00', '4xwxA00', '1x11A00', '1p3rC00', '2yt0A01',
           '1wguA01', '1x11B00', '2m38A00', '3f0wA00', '2ej8B00',
           '4dbbA00', '1aqcA00', '3sv1B00', '3dxeA00', '2yszA01', '3so6A00',
           '3d8dA00', '1aqcB00', '4l6eA00', '1k5dB00', '1xkeA00',
           '2ec1A00', '3wyfE00', '2crfA01', '5cllB00', '3oanA00', '2y8gB00',
           '4hatB00', '1xodB00', '1qc6A00', '1mkeA00', '1ddwA00', '1egxA00',
           '2p8vA00', '1ddvA00', '3syxA00', '2jp2A00', '5j3tA00', '4b6hA00',
           '1q67A01', '2lydA00'] ###41

FakeS60 = ['1ntvA00', '4xwxA00', '1p3rC00', '2yt0A01', '1wguA01',
           '2m38A00', '2ej8B00', '3dxeA00', '3so6A00', '3d8dA00',
           '1aqcB00', '4l6eA00', '1k5dB00', '1xkeA00', '2ec1A00', '3wyfE00',
           '5cllB00', '3oanA00', '2y8gB00', '4hatB00', '1xodB00', '1mkeA00',
           '1ddwA00', '1egxA00', '2p8vA00', '5j3tA00', '4b6hA00', '1q67A01',
           '2lydA00'] ###29


NEWPTBS95 = ['1ntvA00', '4xwxA00', '1x11A00', '1p3rC00', '2yt0A01', '1wguA01',
             '1x11B00', '2m38A00', '3f0wA00', '2ej8B00', '4dbbA00', '1aqcA00',
             '3sv1B00', '3dxeA00', '2yszA01', '3so6A00', '3d8dA00', '1aqcB00']
            ###18

RanBDS95 = ['4l6eA00', '1k5dB00', '1xkeA00', '2ec1A00', '3wyfE00', '2crfA01',
            '5cllB00', '3oanA00', '2y8gB00', '4hatB00'] ###10
EVHS95 = ['1xodB00', '1qc6A00', '1mkeA00', '1ddwA00', '1egxA00', '2p8vA00',
          '1ddvA00', '3syxA00', '2jp2A00'] ###9

DcpS95 = ['5j3tA00', '4b6hA00', '1q67A01', '2lydA00'] ###4

NEWPTBS60 = ['1ntvA00', '4xwxA00', '1p3rC00', '2yt0A01', '1wguA01', '2m38A00',
             '2ej8B00', '3dxeA00', '3so6A00', '3d8dA00', '1aqcB00'] ###11

RanBDS60 = ['4l6eA00', '1k5dB00', '1xkeA00', '2ec1A00', '3wyfE00', '5cllB00',
            '3oanA00', '2y8gB00', '4hatB00'] ###9
EVHS60 = ['1xodB00', '1mkeA00', '1ddwA00', '1egxA00', '2p8vA00'] ###5

DcpS60 = ['5j3tA00', '4b6hA00', '1q67A01', '2lydA00'] ###4


fakeF35 = []
fake2M59 = []
fake12 = []
fakeOM1 = []
fakeOM2 = []
for ID in OM2:
    if ID in FakeS95:
        fakeOM2.append(ID)

fakeOM2.sort()
print(*fakeOM2, sep=", ")

#print(*F21, sep="\n ")