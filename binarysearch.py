# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 12:40:10 2019

@author: harshvardhan
"""

def BinarySearch(Arr,left,right,num):
    if left>right:
        return -1
    mid = (left + right)//2
    match = Arr[mid]
    if num == match:
        return mid
    elif num < match:
        return BinarySearch(Arr,left,mid-1,num)
    else:
        return BinarySearch(Arr,mid+1,right,num)
    
    
    
    
    
l =[1,3,4,2,5]
l.sort()
x = BinarySearch(l,0,len(l)-1,2)