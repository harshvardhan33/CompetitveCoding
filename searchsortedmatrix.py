# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 14:24:10 2020

@author: harshvardhan
"""

matrix = [[1,4,7,12,15,1000],
          [2,5,19,31,32,1001],
          [3,8,24,33,35,1002],
          [40,41,42,44,45,1003],
          [99,100,103,106,128,1004]]

num = 12
row = 0 
flag= 0
column = len(matrix[0])-1

while row<len(matrix) and column>=0:
    if matrix[row][column]>num:
        column-=1
    elif matrix[row][column]<num:
        row+=1
    else:
        flag=1
        break
        
if flag==1:
    print(row,column)
else:
    print("Not found")