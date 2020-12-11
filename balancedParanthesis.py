# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 17:01:12 2020

@author: harshvardhan
"""

s = "[()]]]"

stk = []
op = "{[("
cl = "}])"
flag = True
for i in s:
    if i in op:
        stk.append(i)
    if i in cl:
        if len(stk)==0:
            flag = False
            break
        if i=="}" and stk[-1]=="{":    
            stk.pop()
        elif i=="]" and stk[-1]=="[":
            stk.pop()
        elif i==")" and stk[-1]=="(":
            stk.pop()
        else:
            flag=False
            break
if len(stk)!=0 or flag==False:
    print("False")
else:
    print("True")
        