# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 17:59:59 2020

@author: harshvardhan
"""

arr = [1,3,5,8,9,2,6,7,6,8,9]

maxReach = arr[0]
steps = arr[0]
jumps = 1

for i in range(1,len(arr)):
    # 1. When you reach the last element
    if i==len(arr)-1:
        break    
    # 2. Update the maxReach
    maxReach = max(maxReach,i+arr[i])    
    # 3. Decrement the steps 
    steps-=1    
    # 4. If steps become 0
    if steps==0:
        jumps+=1 # increment the jump
        # when currIndex > maxReach is failure
        if i>=maxReach:
            print(-1)
            break
        steps = maxReach - i
print(jumps)
        
        