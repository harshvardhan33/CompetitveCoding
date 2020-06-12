# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 08:21:35 2019

@author: harshvardhan
"""


"""Recursive Solution of Fib
O(2^N) - Time complexity 
O(N) - Space complexity

def nthFibRec(n):
    if n==2:
        return 1
    if n==1:
        return 0
    else:
        return nthFibRec(n-1) + nthFibRec(n-2)
        
"""

""" Dynamic Solution 
time - O(n)
space - O(n)

def nthFibDynam(n):
    
    if n in hs:
        return hs[n]
    else:
        hs[n] = nthFibDynam(n-1)+ nthFibDynam(n-2)
        return hs[n]

"""

def nthFibIter(n):
    lastTwo = [0,1]
    counter = 3
    while counter <= n :
        nextFib = lastTwo[0]+lastTwo[1]
        lastTwo[0]=lastTwo[1]
        lastTwo[1]= nextFib
        counter+=1
        
    return lastTwo[1] if n>1 else lastTwo[2]


N = 5
#term1 = nthFibRec(5)

#hs={1:0,2:1}
#term2 = nthFibDynam(5)
term3 = nthFibIter(5)