# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 21:17:54 2019

@author: harshvardhan
"""

s1 = "neman"
flag = 1
for i in range(len(s1)):
    if s1[i]==s1[len(s1)-1-i]:
        flag = 0
    else:
        flag=1
        break

if flag == 0:
    print("Yes Pallindrome")
else:
    print("Not the pallindrome")