# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 20:35:50 2020

@author: harshvardhan
"""

def isSafe(row,col):
    if row>=0 and row<size_x and col>=0 and col<size_y and board[row][col]==1:
        return True
    return False

def solveMaze(row,col):
    if row==size_x-1 and col==size_y-1 and board[row][col]==1:
        solution[row][col] = 1
        return True
    
    if isSafe(row,col)==True:
        solution[row][col]=1
        
        #go into down direction
        if solveMaze(row+1,col):
            return True
        
        #go into right direction
        if solveMaze(row,col+1):
            return True
        
        
        #go into right diagonal up
        if solveMaze(row-1,col+1):
            return True      
        
        
        #go into right diagonal down
        if solveMaze(row+1,col+1):
            return True
        
        solution[row][col]=0
    
    return False


board = [[1,0,0,0],[1,1,1,1],[0,0,0,1],[1,1,1,1]]
solution = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
size_x,size_y = len(board),len(board[0])

if solveMaze(0,0):
    for i in solution:
        print(*i)
else:
    print("No solution ")