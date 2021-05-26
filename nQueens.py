# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 19:22:49 2020

@author: harshvardhan
"""


def isPossible(n,row,col,board):
    # We need to check three ways 
    # Check above in same column
    for i in range(row-1,-1,-1):
        if board[i][col]==1:
            return False   
    # check above left in diagonal
    i = row-1 
    j = col-1 
    while i>=0 and j>=0:
        if board[i][j]==1:
            return False
        i-=1
        j-=1
    # check above right in diagonal
    i = row-1
    j = col-1
    while i>=0 and j<n:
        if board[i][j]==-1:
            return False
        i-=1
        j+=1        
    return True

def nQueenHelper(n,row,board):
    if row==n: #if reached the last row
        return True
    #Place at all possible position and move to smaller problem 
    for col in range(n):
        if isPossible(n,row,col,board):
            board[row][col] = 1
            if nQueenHelper(n, row+1,board)==True:
                return True
            board[row][col]=0
    return False            

def placeNQueens(n,board):    
    if nQueenHelper(n,0,board)==True:
        print(board)
N = 8
board = [[0 for i in range(N)]for j in range(N)]
placeNQueens(N,board)