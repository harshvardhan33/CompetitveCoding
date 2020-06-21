# -*- coding: utf-8 -*-
"""
Created on Sat May 30 10:21:01 2020

@author: harshvardhan
"""



def update(f_tree,n,index,value):
    """
    Updation takes place 
    index+=index&(-index)
    """
    index+=1
    while index<=n:
        f_tree[index]+=value
        index+=index&(-index)


def query(f_tree,index):
    """
    Updation takes place 
    index+=index&(-index)
    """
    index+=1
    sm = 0
    while index>0:
        sm+= f_tree[index]
        index = index - (index&(-index))
    
    return sm



n = int(input())
arr = [0]*(n+1)
f_tree = [0]*(n+1)
for i in range(1,n+1):
    arr[i] = int(input())
    update(f_tree ,n,i,arr[i])
    
print("Queries : Sum of first 5 Elements")
ans1 = query(f_tree ,5)
print(ans1)

    
print("Queries : Sum of 2-7 Elements")
"""
Take out sum of elements of 0-7
Take out sum of element  of 0-2
Subtract them to get the answer
"""
ans2 =query(f_tree,7) - query(f_tree,2)
print(ans2)


    