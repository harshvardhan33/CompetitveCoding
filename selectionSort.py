# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 18:00:14 2019

@author: harshvardhan
"""

def selectionSort(array):
    currIdx = 0
    while currIdx < len(array)-1:
        smallIdx = currIdx
        for i in range(currIdx+1,len(array)):
            if array[smallIdx] > array[i]:
                smallIdx = i
            
        temp = array[currIdx]
        array[currIdx] = array[smallIdx]
        array[smallIdx] = temp 
        currIdx+=1
    
    return array
    



ls = [8,9,5,5,6,2,3]
ls = selectionSort(ls)