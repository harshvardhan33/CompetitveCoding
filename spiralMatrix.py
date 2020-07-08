# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 20:42:07 2020

@author: harshvardhan
"""

a = [[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]]

top = 0 
left = 0 
right = len(a)-1
down = len(a)-1
direc = 0 

while top<=down and left<=right:
    if direc==0:
        for i in range(left,right+1):
            print(a[top][i])
        top+=1
        
    if direc==1:
        for i in range(top,down+1):
            print(a[i][right])
        right-=1

    if direc==2:
        for i in range(right,left-1,-1):
            print(a[down][i])
        down-=1
        
    if direc==3:
        for i in range(down,top-1,-1):
            print(a[i][left])
        left+=1
    
    direc = (direc+1)%len(a)
    
    