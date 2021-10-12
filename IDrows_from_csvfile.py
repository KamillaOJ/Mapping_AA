#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 15:27:04 2021

@author: kamilla
"""

### find the cath ID of the "fake" PH domains from a csv file

with open ("/Users/Kamilla/documents/data/Fake_PH/Fake_PH.csv", "r") as fakePH:
    dom = fakePH.readlines()
    domID = []
    for ID in dom:
        domID.append(ID.strip())
        
        
    print(domID)