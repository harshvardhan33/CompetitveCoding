# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 22:10:18 2020

@author: harshvardhan
"""





arr = [[2,1,0,2,1],[1,0,1,2,1],[1,0,0,2,1]]
r = len(arr)
c = len(arr[0])
q = []
fresh = 0
time = 0
for i in range(r):
    for j in range(c):
        if arr[i][j]==2:
            q.append([i,j])
        if arr[i][j]==1:
            fresh+=1
while len(q):
    n = len(q)
    for i in range(n):
        x = q[0][0]
        y = q[0][1]
        q.pop(0)
        if x>0 and arr[x-1][y]==1: arr[x-1][y]=2;fresh-=1;q.append([x-1,y])        
        if y>0 and arr[x][y-1]==1: arr[x][y-1]=2;fresh-=1;q.append([x,y-1])      
        if x<r-1 and arr[x+1][y]==1: arr[x+1][y]=2;fresh-=1;q.append([x+1,y])        
        if y<c-1 and arr[x][y+1]==1: arr[x][y+1]=2;fresh-=1;q.append([x,y+1])
        if len(q):
            time+=1
if fresh==0:
    print(1)
else:
    print(-1)
            
 