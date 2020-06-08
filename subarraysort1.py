# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 11:57:36 2019

@author: harshvardhan
"""
ls = [1,2,4,7,10,11,7,12,6,7,16,18,19]

n = len(ls)
mn = float('inf')
mx =  float('-inf')
for i in range(n-1):
    if(i==0 and ls[i]<=ls[i+1]):
        continue
    if(i==n and ls[i]>=ls[i-1]):
        continue       
    elif(ls[i-1]<=ls[i]<=ls[i+1]):
        continue
    else:
        if ls[i]<=mn:
            mn = ls[i]
        if ls[i]>=mx:
            mx = ls[i]

front = 0
end = len(ls)-1
while(mn>=ls[front]):
    front+=1
while(mx<=ls[end]):
    end-=1
print([front,end])