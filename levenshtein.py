# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 23:37:03 2019

@author: harshvardhan
"""

def levenshtein(str1,str2):
    res = [[i for i in range(len(str2)+1)]for j in range(len(str1)+1)]
    for i in range(1,len(str1)+1):
        res[i][0]=res[i-1][0]+1
    for i in range(1,len(str1)+1):
        for j in range(1,len(str2)+1):
            if str1[i-1]==str2[j-1]:
                res[i][j]=res[i-1][j-1]
            else:
                res[i][j]=1+min(res[i-1][j-1],res[i-1][j],res[i][j-1])
                
    return res[-1][-1]            
        
str1 = "abc"
str2 = "yabd"
x=levenshtein(str1,str2)
print(x)