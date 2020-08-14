# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 12:39:54 2020

@author: harshvardhan
"""


def unset_Bit(num,k):
    mask = ~(2**k) #1<<k
    num = mask&num
    print("Number in decimal ", num)
    print("Number in binary ", bin(num)[2:])
def set_Bit(num,k):
    mask = 2**k  # 1<<k
    num = mask|num
    print("Number in decimal ", num)
    print("Number in binary ", bin(num)[2:])

N=4
k=0
set_Bit(N, k)
unset_Bit(N, k)

    
