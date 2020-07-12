# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 13:39:42 2020

@author: harshvardhan
"""

class Triplet:
    def __init__(self):
        self.x = None
        self.y = None 
        self.gcd = None
        

def extendedEuclid(a,b):
    #Base Case
    if b==0:
        ans = Triplet()
        ans.x = 1
        ans.y = 0
        ans.gcd = a
        return ans
    smallAns = extendedEuclid(b, a%b)
    ans = Triplet()
    ans.gcd = smallAns.gcd
    ans.x = smallAns.y
    ans.y = smallAns.x - (a//b)*smallAns.y
    return ans


a = 16 
b = 10 

final = extendedEuclid(a, b)
print(final.x,final.y,final.gcd)        