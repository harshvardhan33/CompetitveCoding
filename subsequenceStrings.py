# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 23:08:58 2020

@author: harshvardhan
"""

s = "abc"
sub = [""]
for ele in s:
    for i in range(len(sub)):
        curr = sub[i]
        sub.append(curr+ele)