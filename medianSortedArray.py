# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 17:45:37 2020

@author: harshvardhan
"""

arr = [1, 12, 15, 26, 38] 
brr = [2, 13, 17, 30, 45] 


n = len(arr)
m = len(brr)

begin1 = 0 
end1 = n

while begin1<=end1:
    i1 = (begin1+end1)//2
    i2 = (n+m+1)//2-i1
    
    min1= (float("inf") if i1==n else arr[i1])
    max1= (float("-inf") if i1==0 else arr[i1-1])
    
    min2=(float("inf") if i2==m else brr[i2])
    max2=(float("inf") if i1==0 else brr[i2-1])
    
    
    if max1<=min2 and max2<=min1:
        if (n-m)%2==0:
            print((max(max1,max2)+min(min1,min2))//2)
            break
        else:
            print(max(max1,max2))
            break
    elif max1>min2:
        end1=i1-1
    else:
        begin1=i1+1
        