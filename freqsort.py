# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 15:15:30 2020

@author: harshvardhan
"""

s = "tree"

dc={}

for i in s:
    if i not in dc:
        dc[i]=1
    else:
        dc[i]+=1
  
dc = {k:v for k,v in sorted(dc.items(),key = lambda x:x[1],reverse=True)}

ans = ""
for i,j in dc.items():
    ans+=(i*j)