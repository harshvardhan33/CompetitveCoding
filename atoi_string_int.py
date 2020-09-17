# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 18:11:07 2020

@author: harshvardhan
"""



s="18889"
num = 0
for i in range(len(s)):
    digit = ord(s[i])-ord("0")
    num+=(10**(len(s)-i-1)*digit)
print(num)    