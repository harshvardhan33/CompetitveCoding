# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 13:51:18 2020

@author: harshvardhan
"""
intervals = [[1,4],[0,2],[3,5]]
intervals.sort(key = lambda x:x[0])
i = 1
while i<len(intervals):
    prev = intervals[i-1]
    curr = intervals[i]
    if curr[0]<=prev[1]:
        prev[0] = min(prev[0],curr[0])
        prev[1] = max(prev[1],curr[1])
        intervals.pop(i)
    else:
        i+=1
print(intervals)