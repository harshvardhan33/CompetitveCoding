# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 21:11:08 2020

@author: harshvardhan
"""



s1 = input("Enter the first string : ")
s2 = input("Enter the first string : ")

dc1={}
dc2={}
for i in s1:
    if i not in dc1:
        dc1[i] = 1
    else:
        dc1[i]+=1
        
for i in s2:
    if i not in dc2:
        dc2[i]=1
    else:
        dc2[i]+=1

if dc1==dc2:
    print("Yes Anagrams")
else:
    print("Not Anagrams")