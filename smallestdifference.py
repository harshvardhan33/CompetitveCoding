# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 09:18:00 2019

@author: harshvardhan
"""

def SmallestDiff(A,B):
    A.sort()
    B.sort()
    left = 0
    right = 0
    current = float("inf")
    smallest = float("inf")
    while(left<len(A) and right<len(B)):
        firstNum = A[left]
        secondNum = B[right]
        if(firstNum<secondNum):
            current = secondNum - firstNum
            left+=1
        elif(firstNum>secondNum):
            current = firstNum - secondNum
            right+=1
        else:
            return[firstNum,secondNum]
        
        if(smallest>current):
            smallest = current
            smallestPair = [firstNum,secondNum]
    
    return smallestPair
    
    
    
    
    
    
a = [-1,5,10,20,28,3]
b = [26,134,135,15,17]

ans = SmallestDiff(a,b)
print(ans)