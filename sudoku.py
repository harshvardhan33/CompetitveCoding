# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 14:22:30 2020

@author: harshvardhan
"""

def checkRow(board,row,num):
    for i in range(9):
        if board[row][i]==num:
            return False
    return True
def checkCol(board,col,num):
    for i in range(9):
        if board[i][col]==num:
            return False
    return True
def checkGrid(board,row,col,num):
    for i in range(3):
        for j in range(3):
            if board[row+i][col+j]==num:
                return False
    return True
def isValidInsert(board,row,col,num):
    ans1 = checkRow(board,row,num)
    ans2 = checkCol(board,col,num)
    ans3 = checkGrid(board,row-row%3,col-col%3,num)    
    if (ans1 and ans2 and ans3):
        return True
    return False
def checkEmpty(board,l):
    for i in range(9):
        for j in range(9):
            if board[i][j]==0:
                l[0] = i 
                l[1] = j
                return True
    return False
def solveSudoku(board):
    l = [0,0]
    if checkEmpty(board,l)==False:
        return True
    row = l[0]
    col = l[1]
    for num in range(1,10):
        if isValidInsert(board,row,col,num):
            board[row][col]=num
            if solveSudoku(board):
                return True
            board[row][col]=0
    return False
N=9
board = [[0 for i in range(9)]for j in range(9)]
if solveSudoku(board)==True:
    for i in range(len(board)):
        print(*board[i])
else:
    print("No Solution")    


