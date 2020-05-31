# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 01:31:49 2019
(({}()())[])
@author: harshvardhan
"""

exp = list(input())
stk = []
openbrck = "([{"
closingbrck = ")}]"
dc = {")":"(","}":"{","]":"["}
for i in exp:
    if i in openbrck:
        stk.append(i)
        continue
    elif i in closingbrck:
        if len(stk)==0:
            print("No")
            break
        if stk[-1]==dc[i]:
            stk.pop()
        else:
            print("No")
            break
        
if len(stk)==0:
    print("Yes")
        