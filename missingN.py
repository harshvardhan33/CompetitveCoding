# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 13:02:42 2020

@author: harshvardhan
"""

arr = [9,6,4,2,3,5,7,0,1]
total = len(arr)*(len(arr)+1)//2
actual = sum(arr)
print(total -actual)