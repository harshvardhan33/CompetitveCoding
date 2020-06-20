# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 11:44:46 2019
@author: harshvardhan
"""

scores = [8,4,2,1,3,6,7,9,5]
rewards = [1 for _ in scores]

for i in range(1,len(scores)):
    j = i-1
    if scores[i]>scores[j]:
        rewards[i] = max(rewards[i],rewards[j]+1)
for i in range(len(scores)-2,-1,-1):
    j = i+1
    if scores[i]>scores[j]:
        rewards[i] = max(rewards[i],rewards[j]+1)


print(sum(rewards))