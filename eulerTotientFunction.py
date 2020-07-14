# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 10:24:27 2020

@author: harshvardhan
"""



n = 100 
phi = [i for i in range(n+1)]

for i in range(2,n+1):
    if phi[i]==i:
        phi[i]=i-1
        start = i
        for j in range(i*2,n+1,i):
            phi[j] = (phi[j]*(i-1))//i
    

for i in range(1,11):
    print(phi[i])