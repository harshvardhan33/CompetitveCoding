# -*- coding: utf-8 -*-
"""
Created on Fri May 28 12:14:57 2021

@author: harshvardhan
"""

arr = [1,1,2,3,3,4,4,8,8]
xor = 0 
for i in arr:
    xor = xor^i
print(xor)

# Binary Search Approach 
# odd index and even index approach 

""" 
1 1 | 2 3 3 4 4 8 8
    
Left Half 
1st instance : odd idx
2nd instance : even idx

Right Half
1st instance : even idx
2nd instance : odd idx
"""


print("Binary Search Approach 1 ")
left = 0 
right = len(arr)-2

while left<=right:
    mid = (left+right)//2
    # If you are on odd index : second appearance
    if mid%2==1: 
        if arr[mid-1]==arr[mid]: # in left half
            left = mid+1
        else: # in right half
            right = mid-1
    # If you are on even index : first appearance
    elif mid%2==0:
        if arr[mid+1]==arr[mid]:# in left half
            left = mid+1
        else: # in right half 
            right = mid-1

print(left)

print("Binary Search Approach 2 ")
left = 0 
right = len(arr)-2
while left<=right:
    mid = (left+right)>>1
    if arr[mid]==arr[mid^1]:
        left = mid+1
    else:
        right = mid-1


print(left)
