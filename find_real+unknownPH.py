#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 14:17:00 2021

@author: kamilla
"""




"""Get the cathID from the protein family accession number from RCSB PDB"""
#Find the confirmed PH domains from CATH 2.30.29.30 and store them by cluster
#Do the same for unconfimermed domains in 2.30.29.30
#Find out which PH domains in the datasets used in the master project are confirmed PH or unknown
import os, glob

RealPH = "5H3D_1,2MDX_1,6BBQ_1,2YS1_1,6D8Z_1,6BBP_1,6FSF_1,1BTK_1,1FB8_1,4NSW_1,1XX0_1,6HHF_1,6HHG_1,2YRY_1,3KSY_1,4K81_1,3KRW_1,3KRX_1,4CKH_1,2COD_1,4CKG_1,4GZU_1,1FAO_1,1BAK_1,2DA0_1,2Q13_1,3VIA_1,2Z0O_1,2Z0P_1,6TVN_1,3AJ4_1,7K7Z_1,6C2Y_1,3ZYS_3,5A3F_1,4KVG_2,1XDV_1,3A8Q_1,3A8P_1,3A8N_1,6HHH_1,6HHJ_1,2J59_2,3HW2_2,7K7L_1,6U7C_1,6HHI_1,3TCA_1,5JJD_1,6TUH_1,4XH9_1,1X1F_1,3PP2_1,1UNR_1,2COF_1,3TFM_1,2DTC_1,3PVW_1,3PVU_1,1P6S_1,6F24_1,5HE3_1,5HE2_1,5HE1_1,5HE0_1,1UNP_1,6DLU_1,1WGQ_1,1UPR_1,3HK0_1,1PLS_1,2P0H_1,1WG7_1,2P0F_1,1NTY_1,2I5F_1,2I5C_1,3CXB_2,1B55_1,1KZG_1,1BWN_1,2UVM_1,6E31_1,1FHX_1,1FHW_1,1PMS_1,3LJU_1,1DRO_1,1U27_1,3FEH_1,1AWE_1,2DYN_1,2ELB_1,5C5B_2,5C5B_1,2KCJ_1,5C6R_1,2UZS_1,2Y7B_1,2UZR_1,3RCP_1,4A6K_1,3CIK_1,2DHK_1,2DHI_1,2DHJ_1,2LG1_1,2LUL_1,2DX1_1,3NSU_1,4D0N_2,4UUD_2,5KCV_1,4A5K_1,6O6H_1,3KY9_1,1WI1_1,4MT6_1,1KZ7_1,6NF1_1,1QQG_1,2P0D_1,5U77_1,4GN1_1,1EAZ_1,5U78_1,4F7H_1,4GMV_1,1UPQ_1,4A6F_1,4A6F_2,4UUK_2,6NFA_1,5UKK_1,4A6H_1,5UKM_1,5UKL_1,3MPX_1,2X18_1,2DFK_1,1FGY_1,1FGZ_1,6NEW_1,6DLV_1,1UNQ_1,4PNK_1,3UZS_1,3UZT_1,1YM7_1,2YS3_1,2NZ8_2,6BCA_2,2D9Z_1,2D9X_1,4KAX_2,2D9V_1,3ZVR_1,6TSE_1,2DKP_1,2D9Y_1,2PZ1_1,1U5E_1,1U5F_1,6BNM_1,1DBH_1,6OLU_1,1V88_1,1X05_1,3MDB_2,2DN6_1,4K2P_1,1U5D_1,6TT2_1,4HHV_1,2RSG_1,4H8S_1,1DYN_1,3SNH_1,2LKO_1,2R09_1,3PSC_1,1XD4_1,1ZM0_1,3FM8_2,2R0D_1,4H6Y_1,1FOE_1,4K2O_1,5C79_1,6F8E_1,1U29_1,1V5P_1,1V61_1,1V5M_1,1RJ2_1,3BJI_1,6U3G_1,5MR1_1,5WG5_1,2BCJ_1,5WG4_1,4MK0_1,7C3M_1,3O96_1,2OTX_1,1H10_1,1U2B_1,1LB1_1,5WG3_1,4EJN_1,1V89_1,2VRW_2,4Y94_1,6U3E_1,1U5G_1,3V5W_1,4Y93_1,1X1G_1,1OMW_1,6S9X_1,6S9W_1,1V5U_1,5L81_1,4MT7_1,4BBK_1"

realPH = []
lrealPH = []

lrealPH.append(RealPH.split(","))

for ID in lrealPH:
    for letter in ID:
        realPH.append(letter[0:4])

allPH = []
realPHID = []

folder_path = "/Users/Kamilla/documents/data/all_PH_raw"
for filename in glob.glob(os.path.join(folder_path, '*.pdb')):
    with open (filename, "r") as f:
        allPH.append(filename[41:48])
 
for code in allPH:
    if code[0:4].upper() in realPH:
        realPHID.append(code)         
        
print(realPHID)
print(len(realPHID))
        
for code in realPHID:
    print(code)
    
realPHcath = ['1fgzA00', '2dynA00', '2i5fA00', '1unpA00', '3aj4B00', '1dbhA02',
              '5c5bA02', '2dtcB00', '1xd4A02', '2dhiA00', '3a8pA01', '4gn1D02',
              '2x18G00', '4a6kB00', '4a5kC00', '3a8pC01', '4a5kA00', '1b55B00',
              '5he2A05', '2x18E00', '2kcjA00', '4h8sD02', '5kcvA01', '5c5bC02',
              '3viaB00', '3bjiB02', '3pp2B00', '1u5dD00', '1eazA00', '2elbA02',
              '3cikA05', '1plsA00', '4y94A00', '2dn6A00', '1wg7A01', '1bwnA00',
              '1droA00', '5he0A05', '5c6rA00', '1fhwA00', '4a6kD00', '2x18A00',
              '1qqgA02', '4gn1B02', '4k2pC01', '1pmsA00', '2rsgA00', '3rcpA00',
              '4bbkA00', '1v5mA00', '4h8sB02', '1unrA00', '3ky9B03', '2x18C00',
              '2dhkA01', '1v88A00', '4gzuB03', '4k2pA01', '2r0dA03', '1qqgA01',
              '1wgqA00', '4gzuB02', '4mk0A05', '1u5dB00', '1v5uA00', '1faoA00',
              '4y94C00', '1xd4B02', '4kaxB00', '2dtcA00', '3pvuA05', '5c5bB02',
              '1rj2J02', '4a6kA00', '2x18D00', '1lb1E02', '1uprA00', '3a8pB01',
              '2dynB00', '1omwA05', '2lg1A02', '1u5fA01', '1x05A00', '1v61A00',
              '3aj4A00', '4y94D00', '2ys1A00', '3tfmA02', '3bjiA02', '1aweA00',
              '1p6sA00', '2uzsA00', '3krwA05', '2d9yA00', '2q13A02', '3pp2A00',
              '2x18F00', '4a6kC00', '1b55A00', '2z0oA02', '2cofA00', '4a5kB00',
              '4k2pD01', '1lb1G02', '3cxbB00', '1u29A00', '2yryA00', '3viaA00',
              '3tfmA01', '1lb1C02', '2nz8B02', '4gn1A02', '2codA01', '3a8pD01',
              '2x18B00', '1x1gA00', '1qqgB02', '4h8sC02', '5c5bD02', '1xx0A00',
              '4y94B00', '1u27A00', '1fhwB00', '5c6rB00', '1u5dC00', '1bwnB00',              
              '1u5dA00', '4gzuA02', '1qqgB01', '1h10A00', '3pvwA05', '3ksyA03',
              '2ys3A00', '4h8sA02', '2r0dB03', '4gn1C02', '1lb1A02', '4k2pB01',
              '4gzuA03', '4a5kD00', '2lulA00', '3ky9A03', '1bakA00', '2bcjA05',
              '2j59N00', '1kz7C02', '1dynB00', '1btkA00', '1fb8A00', '4a6hD00',
              '3pscA05', '2r09A03', '5he3A05', '3a8qC01', '2z0pA00', '4ejnA01',
              '5l81A00', '1fhxA00', '4k81E02', '2p0hA00', '4a6fB00', '4mt7A02',
              '4k81G02', '2z0pC00', '3a8qA01', '1zm0B00', '2p0dA00', '1u5gB01',
              '5c79A00', '4d0nB02', '1kz7A02', '4hhvA00', '1unqA00', '4pnkA05',
              '2p0fA00', '2dhjA00', '1rj2D02', '3fehA02', '4a6hB00', '2otxB02',
              '2dx1A03', '2lkoA00', '3hk0A02', '4k81C02', '1fgyA00', '3fehA03',
              '2dfkA02', '1v89A00', '1kzgC02', '3tcaA02', '2dfkC02', '3nsuA00',
              '3v5wA05', '1kzgA02', '3fm8C02', '4k81A02', '3zvrA03', '1u2bA00',
              '3mdbD02', '4f7hA00', '3mdbD03', '2x18H00', '2mdxA00', '3fm8C03',
              '2j59Q00', '4gmvA02', '2i5cB00', '5he1A05', '4nswB02', '1ntyA02',
              '1u5gD01', '1u5eB02', '2z0pB00', '2dkpA01', '2d9xA01', '3fm8D02',
              '1v5pA01', '2da0A00', '1fhxB00', '2j59M01', '3mdbC02', '5l81B00',
              '3mdbC03', '2uzrA00', '3fm8D03', '2r09B03', '1foeE02', '1dynA00',             
              '1btkB00', '1u5gC01', '1rj2A02', '1u5gA01', '5c79B00', '1foeG02',
              '4kvgD02', '4hhvB00', '2j59O00', '3mpxA02', '4a6fA00', '3hw2B00',
              '1zm0A00', '3a8qB01', '3hk0B02', '3ljuX03', '2z0pD00', '3uztA05',
              '2uvmA00', '2otxA02', '1foeC02', '2i5cC00', '4a6hA00', '1rj2G02',
              '3o96A01', '3ljuX02', '1upqA00', '2j59P00', '2pz1A03', '2j59R00',              
              '4kvgB02', '2d9vA01', '3snhA03', '2d9zA01', '1u5eA02', '4nswA02',
              '1foeA02', '2i5cA00', '4a6hC00', '1wi1A01', '2y7bA00', '4gmvB02',
              '1x1fA00', '3nsuB00', '3a8qD01', '4k2oA01', '3tcaB02', '2vrwB02',
              '3krxA05'] ###277

realPHS95 = ['2i5fA00', '1dbhA02', '2dhiA00', '2x18E00', '2kcjA00', '1eazA00',
             '1plsA00', '2dn6A00', '1droA00', '1fhwA00', '3rcpA00', '4bbkA00',
             '1v5mA00', '2dhkA01', '4gzuB03', '1qqgA01', '1wgqA00', '1v5uA00',
             '1faoA00', '2dtcA00', '3a8pB01', '2lg1A02', '1u5fA01', '1x05A00',
             '1v61A00', '3aj4A00', '2ys1A00', '3tfmA02', '1p6sA00', '2d9yA00',
             '2q13A02', '3pp2A00', '2cofA00', '4k2pD01', '3cxbB00', '1u29A00',
             '2yryA00', '3tfmA01', '2codA01', '1x1gA00', '5c5bD02', '1u5dA00',
             '4gzuA02', '3ksyA03', '2ys3A00', '4gn1C02', '2lulA00', '2j59N00',
             '1kz7C02', '1btkA00', '2p0hA00', '5c79A00', '4d0nB02', '4hhvA00',
             '1unqA00', '2dhjA00', '1fgyA00', '1v89A00', '2dfkC02', '4k81A02',
             '3zvrA03', '4f7hA00', '1ntyA02', '2dkpA01', '2d9xA01', '1v5pA01',
             '2da0A00', '5l81B00', '1dynA00', '3mpxA02', '3hk0B02', '3ljuX03',
             '1foeC02', '4a6hA00', '3ljuX02', '1upqA00', '2pz1A03', '4kvgB02',
             '2d9vA01', '2d9zA01', '4nswA02', '1wi1A01', '2y7bA00', '1x1fA00',
             '2vrwB02'] ###85

realPHS60 = ['2i5fA00', '1dbhA02', '1eazA00', '1plsA00', '2dn6A00', '1droA00',
             '3rcpA00', '4bbkA00', '1v5mA00', '2dhkA01', '4gzuB03', '1qqgA01',
             '1wgqA00', '1v5uA00', '1faoA00', '2dtcA00', '2lg1A02', '1u5fA01',
             '1v61A00', '3aj4A00', '3tfmA02', '2d9yA00', '2q13A02', '3pp2A00',
             '2cofA00', '4k2pD01', '3cxbB00', '3tfmA01', '2codA01', '1x1gA00',
             '1u5dA00', '4gzuA02', '3ksyA03', '2lulA00', '2j59N00', '1kz7C02',
             '1btkA00', '2p0hA00', '5c79A00', '4d0nB02', '4hhvA00', '1unqA00',
             '1fgyA00', '1v89A00', '2dfkC02', '1ntyA02', '2dkpA01', '2d9xA01',
             '1v5pA01', '5l81B00', '1dynA00', '3mpxA02', '3hk0B02', '3ljuX03',
             '1foeC02', '4a6hA00', '3ljuX02', '1upqA00', '2pz1A03', '4kvgB02',
             '2d9vA01', '4nswA02', '1wi1A01', '2y7bA00', '1x1fA00', '2vrwB02']
            ###66
            
FakeS95 = ['1ntvA00', '4xwxA00', '1x11A00', '1p3rC00', '2yt0A01', '2q13A02',
           '1wguA01', '1x11B00', '2m38A00', '5c5bD02', '3f0wA00', '2ej8B00',
           '4dbbA00', '1aqcA00', '3sv1B00', '3dxeA00', '2yszA01', '3so6A00',
           '2dyqA00', '3d8dA00', '1aqcB00', '4l6eA00', '1k5dB00', '1xkeA00',
           '2ec1A00', '3wyfE00', '2crfA01', '5cllB00', '3oanA00', '2y8gB00',
           '4hatB00', '1xodB00', '1qc6A00', '1mkeA00', '1ddwA00', '1egxA00',
           '2p8vA00', '1ddvA00', '3syxA00', '2jp2A00'] ###40

"""All the domains in CATH clusters"""

S95 = ['1aqcA00', '1aqcB00', '1btkA00', '1btnA00', '1dbhA02', '1ddvA00', '1ddwA00',
       '1droA00', '1dynA00', '1eazA00', '1egxA00', '1faoA00', '1fgyA00', '1fhoA00',
       '1fhwA00', '1foeC02', '1h4rA03', '1j0wB00', '1k5dB00', '1kz7C02', '1maiA00',
       '1mixA02', '1mkeA00', '1ntvA00', '1ntyA02', '1p3rC00', '1p5tA00', '1p6sA00',
       '1pfjA00', '1plsA00', '1q67A01', '1qc6A00', '1qqgA01', '1tqzA01', '1txdA02',
       '1u29A00', '1u5dA00', '1u5fA01', '1unqA00', '1upqA00', '1v5mA00', '1v5pA01',
       '1v5uA00', '1v61A00', '1v89A00', '1vu2300', '1w1hD00', '1wgqA00', '1wguA01',
       '1wi1A01', '1wjmA00', '1wvhA00', '1x05A00', '1x11A00', '1x11B00', '1x1fA00',
       '1x1gA00', '1xkeA00', '1xodB00', '1xr0B01', '1y5oA00', '1zc3B00', '1zsqA01',
       '2adzA01', '2aehA03', '2cayB00', '2coaA01', '2cocA01', '2codA01', '2cofA00',
       '2crfA01', '2cy5A00', '2d9vA01', '2d9wA01', '2d9xA01', '2d9yA00', '2d9zA01',
       '2da0A00', '2dfkC02', '2dhiA00', '2dhjA00', '2dhkA01', '2dkpA01', '2dlwA00',
       '2dn6A00', '2dtcA00', '2dx5A00', '2dyqA00', '2ec1A00', '2ej8B00', '2fjlA00',
       '2hthB00', '2i1jA03', '2i5fA00', '2j59N00', '2jp2A00', '2kcjA00', '2kupA01',
       '2lg1A02', '2lulA00', '2lydA00', '2m38A00', '2mfqA00', '2oqbA00', '2p0hA00',
       '2p8vA00', '2pz1A03', '2q13A02', '2rgnB02', '2rloA00', '2rovA00', '2v76B00',
       '2vrwB02', '2vszB02', '2w2xC00', '2x18E00', '2y7bA00', '2y8gB00', '2yf0A01',
       '2yryA00', '2ys1A00', '2ys3A00', '2yszA01', '2yt0A01', '2z0qA02', '2zpyA03',
       '3a8pB01', '3aj4A00', '3au4A04', '3cxbB00', '3d8dA00', '3dxeA00', '3f0wA00',
       '3f5rA00', '3fssA02', '3g9wA02', '3gyoA02', '3gypA02', '3hk0B02', '3hqcA00',
       '3ksyA03', '3ljuX02', '3ljuX03', '3ml4A02', '3ml4C01', '3mpxA02', '3oanA00',
       '3p6aB02', '3pg7A02', '3pp2A00', '3pvlA04', '3qbvB02', '3qijB03', '3qwmA00',
       '3rcpA00', '3so6A00', '3sv1B00', '3syxA00', '3tfmA01', '3tfmA02', '3ulbA01',
       '3voqA00', '3wyfE00', '3zvrA03', '4a6hA00', '4b6hA00', '4bbkA00', '4chjA00',
       '4chmB00', '4d0nB02', '4dbbA00', '4dx8D00', '4ekuA03', '4emoC00', '4f7hA00',
       '4f7uP00', '4gn1C02', '4gxbA03', '4gzuA02', '4gzuB03', '4hatB00', '4hdoA03',
       '4hhvA00', '4iapA01', '4ioyX02', '4k17A01', '4k17B01', '4k17C01', '4k17D01',
       '4k2pD01', '4k81A02', '4khbB01', '4khoB02', '4kvgB02', '4l6eA00', '4nswA02',
       '4pq0A02', '4tyzA00', '4wj7D00', '4wsfA00', '4xwxA00', '4yl8A03', '5c16A01',
       '5c5bD02', '5c79A00', '5cllB00', '5d3xB00', '5efxA00', '5j3tA00', '5jhhA02',
       '5l81B00'] ###211

S60 = ['1aqcB00', '1btkA00', '1btnA00', '1dbhA02', '1ddwA00', '1droA00', '1dynA00',
       '1eazA00', '1egxA00', '1faoA00', '1fgyA00', '1fhoA00', '1foeC02', '1j0wB00',
       '1k5dB00', '1kz7C02', '1maiA00', '1mixA02', '1mkeA00', '1ntvA00', '1ntyA02',
       '1p3rC00', '1pfjA00', '1plsA00', '1q67A01', '1qqgA01', '1tqzA01', '1txdA02',
       '1u5dA00', '1u5fA01', '1unqA00', '1upqA00', '1v5mA00', '1v5pA01', '1v5uA00',
       '1v61A00', '1v89A00', '1w1hD00', '1wgqA00', '1wguA01', '1wi1A01', '1wvhA00',
       '1x1fA00', '1x1gA00', '1xkeA00', '1xodB00', '1xr0B01', '1y5oA00', '1zc3B00',
       '1zsqA01', '2adzA01', '2aehA03', '2cayB00', '2coaA01', '2cocA01', '2codA01',
       '2cofA00', '2cy5A00', '2d9vA01', '2d9wA01', '2d9xA01', '2d9yA00', '2dfkC02',
       '2dhkA01', '2dkpA01', '2dlwA00', '2dn6A00', '2dtcA00', '2dyqA00', '2ec1A00',
       '2ej8B00', '2fjlA00', '2hthB00', '2i5fA00', '2j59N00', '2lg1A02', '2lulA00',
       '2lydA00', '2m38A00', '2mfqA00', '2oqbA00', '2p0hA00', '2p8vA00', '2pz1A03',
       '2q13A02', '2rgnB02', '2rloA00', '2rovA00', '2v76B00', '2vrwB02', '2vszB02',
       '2w2xC00', '2y7bA00', '2y8gB00', '2yf0A01', '2yt0A01', '2z0qA02', '3aj4A00',
       '3au4A04', '3cxbB00', '3d8dA00', '3dxeA00', '3f5rA00', '3fssA02', '3hk0B02',
       '3ksyA03', '3ljuX02', '3ljuX03', '3ml4A02', '3ml4C01', '3mpxA02', '3oanA00',
       '3p6aB02', '3pg7A02', '3pp2A00', '3pvlA04', '3qbvB02', '3qwmA00', '3rcpA00',
       '3so6A00', '3tfmA01', '3tfmA02', '3ulbA01', '3voqA00', '3wyfE00', '4a6hA00',
       '4b6hA00', '4bbkA00', '4chjA00', '4chmB00', '4d0nB02', '4dx8D00', '4ekuA03',
       '4emoC00', '4f7uP00', '4gxbA03', '4gzuA02', '4gzuB03', '4hatB00', '4hdoA03',
       '4hhvA00', '4iapA01', '4ioyX02', '4k17B01', '4k2pD01', '4khbB01', '4kvgB02',
       '4l6eA00', '4nswA02', '4pq0A02', '4tyzA00', '4wj7D00', '4wsfA00', '4xwxA00',
       '4yl8A03', '5c79A00', '5cllB00', '5d3xB00', '5efxA00', '5j3tA00', '5jhhA02',
       '5l81B00'] ###162





            
"""Finding the real PH in S95 and S60 cluster"""
with open ("/Users/Kamilla/documents/data/cath_S95.txt", "r") as cath:
    cath_S95 = []
    lines = cath.readlines()
    for line in lines:
        cath_S95.append(line[0:7])


with open ("/Users/Kamilla/documents/data/cath_S60.txt", "r") as cath:
    cath_S60 = []
    lines = cath.readlines()
    for line in lines:
        cath_S60.append(line[0:7])

for cathid in realPHcath:
    if cathid in cath_S95:
        realPHS95.append(cathid)

print(realPHS95)
print(len(realPHS95))

"""All the motif datasets, orinitaing from S95"""
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

F35_OM1 = ['1tqzA01', '1xkeA00', '2crfA01', '4khbB01', '1maiA00', '2d9zA01',
           '3mpxA02', '4l6eA00', '1p3rC00', '3voqA00']


"""Unknown PH containing motif"""

S95UN = []

F56UN = ['3ml4C01', '4khbB01', '1w1hD00', '3voqA00', '1maiA00', '5d3xB00',
         '1tqzA01', '4chjA00', '2yf0A01', '3au4A04', '2i1jA03', '4yl8A03',
         '2d9wA01'] ###13

F35UN = ['1tqzA01', '4khbB01', '2d9wA01', '3ml4C01', '1maiA00', '3voqA00']
        ###6

M26_1UN = ['1tqzA01', '3ml4C01', '1maiA00', '4khbB01'] ###4 

M59_2UN = ['1btnA00', '1wjmA00', '3ml4C01', '2cy5A00', '2rloA00', '4wsfA00',
           '2vszB02', '3qbvB02', '2d9wA01'] ###9

M1and2UN = ['3ml4C01'] ###1

OM1UN = ['1tqzA01', '1maiA00', '4khbB01'] ###3

OM2UN = ['1btnA00', '1wjmA00', '2cy5A00', '2rloA00', '4wsfA00', '2vszB02',
         '3qbvB02', '2d9wA01'] ###8

# S95OR = []
# OR = []

# for ID in S95:
#     if ID in FakeS95 and ID in realPHS95:
#         OR.append(ID)
        
# #print(S95UN)
# print(OR)

# print(len(realPHS95))
# for ID in realPHS95:
#     print(ID)

realPHS95.sort()
print(*realPHS95, sep= ", ")
print(len(realPHS95))














