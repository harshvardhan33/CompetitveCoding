# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 23:22:23 2020

@author: harshvardhan
"""

a = [[1,0,1],[1,0,1],[1,1,1]]
row = False
col = False


for i in range(len(a)):
    if a[i][0]==0:
        col= True
        break
    
    
for i in range(len(a[0])):
    if a[0][i]==0:
        row= True
        break
        
for i in range(1,len(a)):
    for j in range(1,len(a[0])):
        if a[i][j]==0:
            a[0][i]=0
            a[j][0]=0

for i in range(1,len(a)):
    for j in range(1,len(a[0])):
        if a[i][0]==0 or a[0][j]==0:
            a[i][j]=0


if row==True:
    for i in range(len(a[0])):
        a[0][i]=0
    

if col==True:
    for i in range(len(a)):
        a[i][0]=0