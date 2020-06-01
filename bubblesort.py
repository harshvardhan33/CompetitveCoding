# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 15:42:06 2019

@author: harshvardhan
"""

ls = [8,5,2,9,5,6,3]
N=len(ls)
while(N-1):
    for i in range(len(ls)-1):
        if(ls[i]>ls[i+1]):
            temp = ls[i]
            ls[i] = ls[i+1]
            ls[i+1] = temp
    N-=1 