# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 13:26:53 2020

@author: harshvardhan
"""




c = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
flag = 0

x0 = c[0][0]
x1 = c[1][0]
y0 = c[0][1]
y1 = c[1][1]

dx = x1-x0
dy = y1-y0 

for i in range(len(c)):
    x = c[i][0]
    y = c[i][1]
    
    if dx*(y-y1)!=dy*(x-x1):
        print("False")
        flag = 1
        break

if flag==0:
    print("True")