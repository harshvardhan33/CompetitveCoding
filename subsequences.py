# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 12:32:57 2019

@author: harshvardhan
"""

subsequences = [""]
a = "abc"
for ele in a:
    for i in range(len(subsequences)):
        currentSubset = subsequences[i]
        subsequences.append(currentSubset+ele)     

for i in sorted(subsequences,key=len):
    print(i)