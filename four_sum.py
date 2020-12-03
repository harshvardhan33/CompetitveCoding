# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 20:56:48 2020

@author: harshvardhan
"""

arr= [1,1,1,2,2,3,3,4,4,4]
n = len(arr)
i = 0
j = 0
l = 0 #left
r = len(arr)-1 # right pointer
target = 9
while i<n-3:
    j = i+1
    while j<n-2:
        l = j+1
        r = n-1
        while l<r:
            currSum = arr[i] + arr[j] + arr[l] + arr[r]
            if(currSum)==target:
                print(arr[i],arr[j],arr[l],arr[r],"index are",i,j,l,r)
                l+=1
                r-=1
                while l<r and arr[l]==arr[l+1]:
                    l+=1
                while l<r and arr[r]==arr[r-1]:
                    r-=1
            elif currSum<target:
                l+=1
                while arr[l]==arr[l+1]:
                    l+=1
            elif currSum>target:
                r-=1
                while arr[r]==arr[r-1]:
                    r-=1
        j+=1
        while j<n-2 and arr[j]==arr[j+1]:
            j+=1
    i+=1
    while i<n-3 and arr[i]==arr[i+1]:
        i+=1