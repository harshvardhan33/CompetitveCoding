# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 18:13:04 2020

@author: harshvardhan
"""
def maxheapify(i,size):
    lc = 2*i+1
    rc = 2*i+2
    largest = i 
    if lc<size and arr[largest]<arr[lc]:
        largest = lc
    if rc<size and arr[largest]<arr[rc]:
        largest = rc
    if largest!=i:
        arr[largest],arr[i] = arr[i],arr[largest]
        maxheapify(largest,size)

def buildHeap(arr):
    n = len(arr)
    idx = (n-2)//2 
    for i in range(idx,-1,-1):
        maxheapify(i,n)


arr = [4,10,3,5,1]
buildHeap(arr)