# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 09:35:11 2020

@author: harshvardhan
"""



def reduce(a,b):
    if a==0:
        return b
    res = 0 
    for i in range(len(b)):
        res = (res*10+int(b[i]))%a
    return res
        

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

def compute(a,b):
    num = reduce(a,b)
    return gcd(a,num)





a = 978 
b = str(89798763754892653453379597352537489494736)

answer = compute(a,b)