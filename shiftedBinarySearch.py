# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 15:29:11 2020

@author: harshvardhan
"""

A = [1,0]

left = 0
right = len(A)-1
target =0
ans =-1
while(left<=right):
    middle = (left+right)//2
    if A[middle]==target:
        print("Found it ")
        ans = middle
        break    
    if A[left]<=A[middle]:
        if target>=A[left] and target<A[middle]:
            right = middle-1        
        else:
            left=middle+1    
    else:
        if target<=A[right] and target>A[middle]:
            left=middle+1
        else:
            right=middle-1
