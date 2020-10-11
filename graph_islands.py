# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 17:13:43 2020

@author: harshvardhan
"""


def isSafe(r,c):
    if r>=0 and r<n_rows and c>=0 and c<n_cols:
        return True
    return False
    
def dfs(islands,row,col):
    if isSafe(row,col):
        if islands[row][col]==1:    
            islands[row][col]=2
            dfs(islands,row+1,col)
            dfs(islands,row-1,col)
            dfs(islands,row,col+1)
            dfs(islands,row,col-1)
           
        

islands = [[1,1,0,0,0],[1,1,0,0,0],[0,0,1,0,0],[0,0,0,1,1]]
count = 0 
n_rows = len(islands)
n_cols =  len(islands[0])


for i in range(n_rows):
    for j in range(n_cols):
        if islands[i][j]==1:
            count+=1
            dfs(islands,i,j)
print(count)           