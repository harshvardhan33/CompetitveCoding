# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 10:33:28 2020

@author: harshvardhan
"""

def bit_Trick(num):
    
    if num&(num-1)==0:
        print("Yes power of 2")
    else:
        print("No it is not")


def divide(num):
    while True:
        if num==0:
            print("No it is not")
            break
        elif num==1:
            print("Yes it is")
            break
        else:
            num=num/2
        

def countSetBit(num):
    num = bin(num)
    if num[2:].count("1")==1:
        print("Yes power")
    else:
        print("No power")

num = 65


bit_Trick(num)
divide(num)
countSetBit(num)
