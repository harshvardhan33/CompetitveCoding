# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 18:21:27 2020

@author: harshvardhan
"""

def isPallindrome(s,i,k):
    temp1 = s[i:k]
    temp2 = temp1[::-1]
    if temp1==temp2:
        return True
    return False



def solve(s,i,j):
    global ans
    if i>=j:
        return 0
    if isPallindrome(s,i,j+1):
        return 0
    for k in range(i,j):
        temp = solve(s,i,k)+solve(s,k+1,j)+1
        ans = min(ans,temp)
    return temp
        





ans = float("inf")
s = list("abac")
print(solve(s,0,4))