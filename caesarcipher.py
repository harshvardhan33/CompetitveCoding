# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 10:44:09 2019

@author: harshvardhan
"""

s = "xyz"
k=[]
for i in range(len(s)):
    k.append(chr((ord(s[i]) + 3)%26))
    
    
"""    
    
    
    
    s[i] = chr((ord(s[i]) + 3)%26)
"""