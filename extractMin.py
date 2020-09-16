# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 17:23:15 2020

@author: harshvardhan
"""



# This function removes the minimum 
# element from the heap 

"""
Steps
1- Take the root to last element (swap)
2- Delete the last element
3- Call heapify on root 
"""
def heapify(arr,idx):
    if idx>len(arr) or 2*idx+1>len(arr) or 2*idx+2>len(arr):
        return   
    lc = arr[2*idx+1]
    rc = arr[2*idx+2]
    curr = arr[idx]
    smallest = min(lc,rc,curr)
    if smallest==curr:
        return
    if smallest==lc:
        arr[idx],arr[2*idx+1] = lc,arr[idx]
        heapify(arr,2*idx+1)
    if smallest==rc:
        arr[idx],arr[2*idx+2] = rc,arr[idx]
        heapify(arr,2*idx+2)
    
def extractMin(arr):
    mnVal = arr[0]
    arr[0],arr[-1] = arr[-1],arr[0]
    arr.pop()
    heapify(arr,0)
    return mnVal


arr = [2,3,4,5,6,7,8]
extractMin(arr)