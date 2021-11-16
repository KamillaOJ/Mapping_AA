#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 13:57:00 2021

@author: kamilla
"""

### Motif and non-PH datasets used in the Masterproject "mapping the amino acid composition 
### of the peripheral membrane binding interphase of PH domains"



## Motif datasets

F56 = ['3ml4C01', '2x18E00', '1eazA00', '1p6sA00', '1unqA00', '2i5fA00',
        '1x1gA00', '1x05A00', '1wi1A01', '1fhwA00', '1u29A00', '1fgyA00',
        '1faoA00', '1v5uA00', '4kvgB02', '4hatB00', '5cllB00', '4gn1C02',
        '2dkpA01', '3mpxA02', '4khbB01', '2pz1A03', '1w1hD00', '1v89A00',
        '3voqA00', '1maiA00', '5l81B00', '2ys3A00', '2dhkA01', '5d3xB00',
        '2crfA01', '1tqzA01', '4chjA00', '2yf0A01', '3au4A04', '4l6eA00',
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


## Non-PH datasets


nonPH = ['1shcA00', '1ntvA00', '3d8eB00', '4xwxA00', '1x11A00', '1nu2A00',
         '2nmbA00', '3dxdA00', '1p3rC00', '3d8eD00', '3suzA01', '1p3rA00',
         '1n3hA00', '3dxdC00', '3d8eA00', '1ddmA00', '2yt0A01', '1wguA01',
         '3d8eC00', '1x11B00', '2m38A00', '1p3rB00', '3d8fD00', '3f0wA00',
         '2rozB00', '3d8dB00', '2ej8B00', '1m7eB00', '1wj1A01', '4dbbA00',
         '3d8fB00', '1aqcA00', '2elaA00', '3sv1B00', '3dxeC00', '3dxeA00',
         '1oqnB00', '1m7eC00', '2yszA01', '3so6A00', '1m7eA00', '3d8dA00',
         '2yt1A01', '2ej8A00', '3sv1A00', '2elaB00', '3dxcA00', '1aqcB00', 
         '3d8fA00', '2l1cA00', '3d8fC00', '1oy2A00', '3dxcC00', '3sv1C00',
         '1oqnA00', '4l6eA00', '1k5dB00', '5dh9B00', '1xkeA00', '1rrpD00',
         '2y8fA00', '3wyfB00', '4hb3B00', '5di9B00', '2ec1A00', '2y8fC00',
         '1rrpB00', '1k5gK00', '5dhaB00', '2y8fD00', '5cllD00', '4hawB00',
         '3wyfE00', '2y8fB00', '4hayB00', '4hauB00', '1k5dE00', '1k5gH00',
         '2crfA01', '5cllB00', '5dhfB00', '4hb0B00', '3oanA00', '5jljB00',
         '5clqB00', '1k5dK00', '5clqD00', '1k5gB00', '4hb2B00', '5difB00',
         '3n7cA00', '2y8gA00', '3m1iB00', '4havB00', '4hazB00', '4gmxB00',
         '1k5dH00', '1k5gE00', '4hb4B00', '4haxB00', '2y8gB00', '4hatB00',
         '3n7cB00', '4gptB00', '4wvfB00', '1xodB00', '1i7aD00', '1qc6A00',
         '2iybD00', '1i7aB00', '1evhA00', '1mkeA00', '2iybB00', '1xodA00',
         '2xqnM00', '1qc6B00', '1i2hA00', '1i7aA00', '2iybC00', '2iybA00',
         '1i7aC00', '1ddwA00', '4my6B00', '1egxA00', '1tj6B00', '4my6A00',
         '2ifsA00', '1tj6A00', '2p8vA00', '1ddvA00', '3syxA00', '2jp2A00',
         '2qkmC00', '5kq1A00', '4b6hB00', '2qkmA00', '5j3tA00', '2qkmE00',
         '1q67B01', '2qkmG00', '4b6hA00', '5kq1D00', '1q67A01', '2qklA00',
         '5lopB01', '5kq4D00', '5j3yC00', '5j3yA00', '5j3qC00', '5jp4A00',
         '5j3qA00', '5lonB01', '2lydA00', '5kq4A00']

PTBcath = ['1shcA00', '1ntvA00', '3d8eB00', '4xwxA00', '1x11A00', '1nu2A00', '2nmbA00',
        '3dxdA00', '1p3rC00', '3d8eD00', '3suzA01', '1p3rA00', '1n3hA00', '3dxdC00',
        '3d8eA00', '1ddmA00', '2yt0A01', '1wguA01', '3d8eC00', '1x11B00', '2m38A00',
        '1p3rB00', '3d8fD00', '3f0wA00', '2rozB00', '3d8dB00', '2ej8B00', '1m7eB00',
        '1wj1A01', '4dbbA00', '3d8fB00', '1aqcA00', '2elaA00', '3sv1B00', '3dxeC00',
        '3dxeA00', '1oqnB00', '1m7eC00', '2yszA01', '3so6A00', '1m7eA00', '3d8dA00',
        '2yt1A01', '2ej8A00', '3sv1A00', '2elaB00', '3dxcA00', '1aqcB00', '3d8fA00',
        '2l1cA00', '3d8fC00', '1oy2A00', '3dxcC00', '3sv1C00', '1oqnA00']

RanBDcath = ['4l6eA00', '1k5dB00', '5dh9B00', '1xkeA00', '1rrpD00', '2y8fA00',
             '3wyfB00', '4hb3B00', '5di9B00', '2ec1A00', '2y8fC00', '1rrpB00',
             '1k5gK00', '5dhaB00', '2y8fD00', '5cllD00', '4hawB00', '3wyfE00',
             '2y8fB00', '4hayB00', '4hauB00', '1k5dE00', '1k5gH00', '2crfA01',
             '5cllB00', '5dhfB00', '4hb0B00', '3oanA00', '5jljB00', '5clqB00',
             '1k5dK00', '5clqD00', '1k5gB00', '4hb2B00', '5difB00', '3n7cA00',
             '2y8gA00', '3m1iB00', '4havB00', '4hazB00', '4gmxB00', '1k5dH00',
             '1k5gE00', '4hb4B00', '4haxB00', '2y8gB00', '4hatB00', '3n7cB00',
             '4gptB00', '4wvfB00']

EVHcath = ['1xodB00', '1i7aD00', '1qc6A00', '2iybD00', '1i7aB00', '1evhA00',
           '1mkeA00', '2iybB00', '1xodA00', '2xqnM00', '1qc6B00', '1i2hA00',
           '1i7aA00', '2iybC00', '2iybA00', '1i7aC00', '1ddwA00', '4my6B00',
           '1egxA00', '1tj6B00', '4my6A00', '2ifsA00', '1tj6A00', '2p8vA00',
           '1ddvA00', '3syxA00', '2jp2A00']

Dcpcath = ['2qkmC00', '5kq1A00', '4b6hB00', '2qkmA00', '5j3tA00', '2qkmE00',
           '1q67B01', '2qkmG00', '4b6hA00', '5kq1D00', '1q67A01', '2qklA00',
           '5lopB01', '5kq4D00', '5j3yC00', '5j3yA00', '5j3qC00', '5jp4A00',
           '5j3qA00', '5lonB01', '2lydA00', '5kq4A00'] ###22

#S95

FakeS95 = ['1ntvA00', '4xwxA00', '1x11A00', '1p3rC00', '2yt0A01',
           '1wguA01', '1x11B00', '2m38A00', '3f0wA00', '2ej8B00',
           '4dbbA00', '1aqcA00', '3sv1B00', '3dxeA00', '2yszA01', '3so6A00',
           '3d8dA00', '1aqcB00', '4l6eA00', '1k5dB00', '1xkeA00',
           '2ec1A00', '3wyfE00', '2crfA01', '5cllB00', '3oanA00', '2y8gB00',
           '4hatB00', '1xodB00', '1qc6A00', '1mkeA00', '1ddwA00', '1egxA00',
           '2p8vA00', '1ddvA00', '3syxA00', '2jp2A00', '5j3tA00', '4b6hA00',
           '1q67A01', '2lydA00']

PTBS95 = ['1ntvA00', '4xwxA00', '1x11A00', '1p3rC00', '2yt0A01', '1wguA01',
             '1x11B00', '2m38A00', '3f0wA00', '2ej8B00', '4dbbA00', '1aqcA00',
             '3sv1B00', '3dxeA00', '2yszA01', '3so6A00', '3d8dA00', '1aqcB00']
            ###18

RanBDS95 = ['4l6eA00', '1k5dB00', '1xkeA00', '2ec1A00', '3wyfE00', '2crfA01',
            '5cllB00', '3oanA00', '2y8gB00', '4hatB00'] ###10
EVHS95 = ['1xodB00', '1qc6A00', '1mkeA00', '1ddwA00', '1egxA00', '2p8vA00',
          '1ddvA00', '3syxA00', '2jp2A00'] ###9

DcpS95 = ['5j3tA00', '4b6hA00', '1q67A01', '2lydA00'] ###4











