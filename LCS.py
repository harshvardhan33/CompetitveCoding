# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 08:42:51 2019

@author: harshvardhan
"""
str1 = "abc"
str2 = "zadbc"

lcs = [[0 for i in range(len(str2)+1)] for j in range(len(str1)+1)]

for i in range(1,len(str1)+1):
    for j in range(1,len(str2)+1):
       if str1[i-1]==str2[j-1]:
           lcs[i][j]=lcs[i-1][j-1]+1
       else:
           lcs[i][j]=max(lcs[i-1][j],lcs[i][j-1])
           
    
    
seq = []
i = len(lcs)-1
j = len(lcs[0])-1
while i!=0 and j!=0:
    if lcs[i][j]==lcs[i-1][j]:
        i-=1
    elif lcs[i][j]==lcs[i][j-1]:
        j-=1
    else:
        seq.append(str2[j-1])
        i-=1
        j-=1

print(*reversed(seq))