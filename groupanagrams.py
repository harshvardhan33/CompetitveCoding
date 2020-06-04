# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 13:44:12 2019

@author: harshvardhan
"""

inp = ["yo","act","flop","oy","cat","olfp","tac"]
dc = {}
for i in inp:
    sortedWord = "".join(sorted(i))
    if sortedWord not in dc:
        dc[sortedWord] =[i]
    else:
        dc[sortedWord].append(i)
print([*dc.values()])