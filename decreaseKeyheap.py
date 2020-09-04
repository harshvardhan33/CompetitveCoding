# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 17:55:18 2020

@author: harshvardhan
"""


def decreaseKey(idx,newVal):
    arr[idx]=newVal
    
    while idx!=0 and arr[(idx-1)//2]>arr[idx]:
        arr[idx],arr[(idx-1)//2] = arr[(idx-1)//2],arr[idx]
        idx = (idx-1)//2


arr = [10,20,40,80,100,70]
idx = 3
newVal = 5

decreaseKey(idx,newVal)