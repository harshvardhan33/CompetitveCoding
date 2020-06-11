# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 09:18:35 2019

@author: harshvardhan
"""

"""
There are 3 approaches for this 
1- using 2 for loops  | O(n^2) time | O(1)
2- using hash table     |O(n)   time | O(n)
3- sort and two pointers  |O(nlogn) time | O(1)

"""

def forLoop(l,ans):
    for i in range(len(l)-1):
        for j in range(i+1,len(l)):
            if(l[i]+l[j]==ans):
                return [l[i],l[j]]
    
    return []

def hashTable(l,ans):
    nums = {}
    for i in l:
        if ans - i in nums:
            return [ans-i,i]
        else:
            nums[i]=True
   

def sortSolve(l,ans):
    l.sort()
    left = 0 
    right = len(l) - 1
    while(left < right):
        currentSum=l[left]+l[right]
        if(currentSum==ans):
            return [l[left],l[right]]
        elif(currentSum<ans):
            left+=1;
        else:
            right-=1;    
    
      
l =[6,5,4,3,2,1]
sm = 11
res1 = forLoop(l,sm) # n^2
res2 = hashTable(l,sm) # n
res3 = sortSolve(l,sm) #nlogn + n = nlogn