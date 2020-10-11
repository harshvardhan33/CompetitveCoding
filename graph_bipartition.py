# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 18:40:36 2020

@author: harshvardhan
"""


def usingHash(ls):
    dc1={}
    dc2={}
    for i in ls:
        f,s = i[0],i[1]
        if (f not in dc1 and s not in dc2) and (f not in dc2 and s not in dc1):
            dc1[f]=1
            dc2[s]=1
            continue
        if f in dc1:
            dc2[s]=1
        elif f in dc2:
            dc1[s]=1
    return dc1,dc2


dislikes = [[1,2],[2,3],[2,4],[3,5],[4,5]]
p1,p2= usingHash(dislikes)





