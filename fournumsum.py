# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 14:04:52 2019

@author: harshvardhan
"""

def fournumsum(a,target):
    allpairhash = {}
    quads = []
    for i in range(1,len(a)-1):
        for j in range(i+1,len(a)):
            currSum = a[i]+a[j]
            diff = target - currSum
            if diff in allpairhash:
                for pair in allpairhash[diff]:
                    quads.append(pair+[a[i],a[j]])
        for k in range(0,i):
            currSum = a[i]+a[k]
            if currSum not in allpairhash:
                allpairhash[currSum] = [[a[k],a[i]]]
            else:
                allpairhash[currSum].append([a[k],a[i]])               
              
    return quads
    
arr = [7,6,4,-1,1,2]
target = 16
ans=fournumsum(arr,target)
    