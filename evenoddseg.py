# -*- coding: utf-8 -*-
"""
Created on Tue May 12 13:18:58 2020

@author: harshvardhan
"""

# -*- coding: utf-8 -*-
"""
Created on Tue May 12 12:09:27 2020

@author: harshvardhan
"""
def query0(arr,tree,start,end,tN,idx,value):
    if start==end:
        arr[idx]=value
        if value%2==0:
            tree[tN] = (1,0)
        else:
            tree[tN]= (0,1)
        return
    mid = (start+end)//2
    if idx>mid:
        query0(arr, tree,mid+1, end, 2*tN+2, idx, value)
    else:
        query0(arr, tree, start, mid, 2*tN+1, idx, value)
    
    left = tree[2*tN + 1]
    right= tree[2*tN + 2]
    
    tree[tN] = list(tree[tN])
    tree[tN][0] =left[0] + right[0]
    tree[tN][1] =left[1] + right[1]
    tree[tN] = tuple(tree[tN])
    






def query1(tree,start,end,left,right,idx):
    if left<=start and right>=end:
        return tree[idx][0]
    if end<left or start>right:
        return 0
    mid = (start+end)//2
    a=query1(tree, start, mid, left, right, 2*idx+1) 
    b=query1(tree, mid+1, end, left, right, 2*idx+2)
    result = 0
    result = result+a+b
    return result
    
    
def query2(tree,start,end,left,right,idx):
    if left<=start and right>=end:
        return tree[idx][1]
    if end<left or start>right:
        return 0
    mid = (start+end)//2
    a=query2(tree, start, mid, left, right, 2*idx+1) 
    b=query2(tree, mid+1, end, left, right, 2*idx+2)
    result = 0
    result = result+a+b
    return result
    
def constructST(arr,tree,start,end,idx):
    if end==start:
        # if the num is odd
        if arr[start]%2==1:
            tree[idx] = (0,1)
        # if the num is even
        else:
            tree[idx] = (1,0)
        return tree[idx]
    
    
    mid = (start+end)//2
    
    left = constructST(arr, tree, start, mid, 2*idx+1)
    right = constructST(arr, tree, mid+1, end, 2*idx+2)

    tree[idx] = list(tree[idx])
    tree[idx][0] = tree[idx][0] + left[0] + right[0]
    tree[idx][1] = tree[idx][1] + left[1] + right[1]
    tree[idx] = tuple(tree[idx])
    return tree[idx]









arr = [2,2,2 ,2 ,2 ,2 ,2 ,2, 19, 100]
n = len(arr)
q = 4
tree = [(0,0)]*(4*n)
constructST(arr, tree, 0,n-1, 0)
"""
while q:
    q-=1
    a,l,r = map(int,input().split())
    if a==0:
        query0(arr,tree,0,n-1,l-1,r,0)
    if a==1:
        print(query1(tree, 0, n-1, l, r, 0))
    if a==2:
        print(query2(tree, 0, n-1, l, r, 0))
"""
#print(query1(tree, 0, n-1, 2, 5, 0))
#print(query2(tree, 0, n-1, 1, 4, 0))
query0(arr, tree, 0, n-1, 0, 4, 4)
query0(arr, tree, 0, n-1, 0, 0, 10)
print(query1(tree, 0, n-1, 1, 10, 0))
print(query2(tree, 0, n-1, 2, 10, 0))


