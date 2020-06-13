# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 21:58:43 2020

@author: harshvardhan
"""

ls = [8,5,2,9,7,6,3]
n = 3
# for third largest number index should be 2
# therefore we will -1 from index 
n=n-1
startIdx = 0
endIdx = len(ls)-1

while True:
    pivot = startIdx
    leftIdx = startIdx+1
    rightIdx = endIdx
    
    while(leftIdx<=rightIdx):
        if ls[leftIdx]>ls[pivot] and ls[rightIdx]<ls[pivot]:
            ls[leftIdx],ls[rightIdx] = ls[rightIdx],ls[leftIdx]
        if ls[leftIdx]<=ls[pivot]:
            leftIdx+=1
        if ls[rightIdx]>=ls[pivot]:
            rightIdx-=1
        
    ls[pivot],ls[rightIdx] = ls[rightIdx],ls[pivot]
    if rightIdx == n :
        print(ls[rightIdx])
        break
    elif rightIdx<n:
        startIdx = rightIdx+1
    else:
        endIdx = rightIdx - 1
        