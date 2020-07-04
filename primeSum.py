# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 01:07:13 2020

@author: harshvardhan
"""

A = 4

primes = [True for i in range(A+1)]

for i in range(2,int(A**(1/2))+1):
    if primes[i]:
        for j in range(i*i,A+1,i):
            primes[j]=False
dc = {}
for i in range(2,len(primes)):
    if primes[i] and i not in dc:
        dc[i]=1