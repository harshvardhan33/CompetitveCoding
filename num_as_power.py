# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 19:54:18 2020

@author: harshvardhan
"""
import math
"""
n= 10
flag = 0
for x in range(2,int(math.sqrt(n))+1):
    y = 1
    p = math.pow(x,y)
    while(p<=n and p>0):
        if(p==n):
            print("Yes")
            flag=1
            break
        
        y+=1
        p=math.pow(x,y)
if flag == 0:
    print("No")
"""

#Way two to do the same thing 

n = 36
flag = 0

for i in range(2,int(math.sqrt(n))+1):
    
    f = math.log(n)/math.log(i)
    print(f,int(f))    
    if f - int(f) == 0.0:
        print("True")
        flag=1
        break

if flag==0:
    print("False")
    