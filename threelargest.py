# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 12:58:40 2019

@author: harshvardhan
"""

array = [None,None,None]
main = [141,1,17,-7,-17,-27,18,541,8,7,7]

for i in main:
    num = i
    if(array[2]==None or num>array[2]):
        array[0]=array[1]
        array[1]=array[2]
        array[2]=num
    elif(array[1]==None or num>array[1]):
        array[0]=array[1]
        array[1]=num
    elif(array[0]==None or num>array[0]):
        array[0]==num;