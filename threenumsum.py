# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 13:03:15 2019

@author: harshvardhan
"""
def Three_Num_Sum(l,ans):
    l.sort()
    final = []
    for i in range(len(l)-2):        
        left = i+1
        right = len(l) - 1
        while(left<right):
            currSum = l[i]+l[left]+l[right]
            if(currSum==ans):
                final.append([l[i],l[left],l[right]])
                left+=1
                right-=1
            elif(currSum<ans):
                left+=1
            elif(currSum>ans):
                right-=1
        
    return final

   
l = [12,3,1,2,-6,5,0,-8,-1,6]
sm = 0
result = Three_Num_Sum(l,sm)
print(result)