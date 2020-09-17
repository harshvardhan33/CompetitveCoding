# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 20:55:08 2020

@author: harshvardhan
"""



arr =["ge","geeksforgeeks", "geeks", "geek", "geezer"]
#arr = sorted(arr)
start = arr[0]
finalCount = 100
for i in range(1,len(arr)):
    curr = arr[i]
    count = 0
    for j,k in zip(curr,start):
        if j==k:
            print(j,k)
            count+=1
        else:
            break
    finalCount = min(finalCount,count)
    print("-------")
        
        
        
        
