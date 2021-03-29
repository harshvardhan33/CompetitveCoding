# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 19:34:26 2020

@author: harshvardhan
"""
def isSafe(row,col,n_row,n_col):
    if row<0 or row>=n_row or col<0 or col>=n_col:
        return False
    return True

def floodFill(matrix,row,col,n_row,n_col,source):
     if not(isSafe(row,col,n_row,n_col)):
         return 
     if matrix[row][col]!=source:
         return
     matrix[row][col]=newColor
     floodFill(matrix,row+1,col,n_row,n_col,source)
     floodFill(matrix,row,col+1,n_row,n_col,source)
     floodFill(matrix,row-1,col,n_row,n_col,source)
     floodFill(matrix,row,col-1,n_row,n_col,source)     
     

matrix = [[1,2,1,1],[2,1,1,2],[1,0,1,0]]
row = 1
col = 2
source = matrix[row][col]
newColor = 3
n_row = len(matrix)
n_col = len(matrix[0])
floodFill(matrix, row, col, n_row, n_col, source)

for i in matrix:
    print(*i)
 