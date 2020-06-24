# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 19:25:27 2020

@author: harshvardhan
"""

from math import floor, sqrt 
   
def simpleSieve(limit, primes): 
    mark = [False]*(limit+1) 
      
    for i in range(2, limit+1): 
        if not mark[i]: 
            primes.append(i) 
            for j in range(i, limit+1, i): 
                mark[j] = True
  
  
def primesInRange(low, high): 
    limit = floor(sqrt(high)) + 1
    primes = list() 
    simpleSieve(limit, primes) 
    n = high - low + 1
    mark = [False]*(n+1) 
    for i in range(len(primes)):  
        loLim = floor(low/primes[i]) * primes[i] 
        if loLim < low: 
            loLim += primes[i] 
        if loLim == primes[i]: 
            loLim += primes[i] 
  
        for j in range(loLim, high+1, primes[i]): 
            mark[j-low] = True
    
    for i in range(low, high+1): 
        if not mark[i-low]: 
            print(i) 
  
  

n = int(input())
while n:
    n-=1
    l,r=map(int,input().split())    
    primesInRange(l,r) 