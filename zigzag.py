# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 10:04:16 2020

@author: harshvardhan
"""


def isOutOfBounds(row,col,height,width):
    return row<0 or row>height or col<0 or col>width

A = [[1,3,4,10],[2,5,9,11],[6,8,12,15],[7,13,14,16]]
height =  len(A)-1
width = len(A[0])-1
result = []
row = 0
col = 0
goingDown = True
while not isOutOfBounds(row,col,height,width):
    print(A[row][col])
    result.append(A[row][col])
    if goingDown:
        if col==0 or row==height:
            goingDown = False
            if row==height:
                col+=1
            else:
                row+=1
        else:
            row+=1
            col-=1
    else:
        if row==0 or col==width:
            goingDown = True
            if col==width:
                row+=1
            else:
                col+=1
        else:
            row-=1
            col+=1
            

