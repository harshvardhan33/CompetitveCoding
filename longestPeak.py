# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 21:18:51 2020

@author: harshvardhan
"""

ls = [1,3,2]
peaks = []
maxPeak = 0
for i in range(1,len(ls)-1):
    if ls[i-1]<ls[i]>ls[i+1]:
        
        peaks.append(i)
      
for i in peaks:
    start = i
    left = i
    right = i
    while(i>=1 and ls[i-1]<ls[i]):
        i-=1
    left=i
    i=start
    
    while(i<len(ls)-1 and ls[i]>ls[i+1]):
        i+=1
    right=i    
    maxPeak = max(maxPeak,right-left+1)
    
print(maxPeak)
        
