# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 12:30:29 2020

@author: harshvardhan
"""


def update(p,value):
    tree[p+n] = value
    p = p+n
    i = p 
    while i>1:
        tree[i//2] = tree[i]+tree[i-1]
        i=i//2
    

def query(tree,start,end,left,right,idx):
    #Our query lies completely inside the range
    if left<=start and right>=end:
        return tree[idx]
    if end<left or start>right:
        return 0   
    
    mid = (start+end)//2
    a=query(tree, start, mid, left, right, 2*idx+1) 
    b=query(tree, mid+1, end, left, right, 2*idx+2)
    return a+b
      

def constructST(arr,tree,start,end,idx):
    if start==end:
        tree[idx] = arr[start]
        return arr[start]
    mid = (start+end)//2
    a = constructST(arr, tree, start, mid, idx*2+1)
    b = constructST(arr, tree, mid+1, end, idx*2+2)
    tree[idx] = a+b
    return tree[idx] 

arr = [1,2,3,4,5]
n = len(arr)
tree = [None]*(2*n)
constructST(arr,tree,0,n-1,0)
print(query(tree,0,n-1,1,5,0))
