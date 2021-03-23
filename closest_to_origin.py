# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 01:52:14 2020

@author: harshvardhan
"""
points = [[3,3],[5,-1],[-2,4]]
dist = []
for i in points:
    d=(i[0]**2+i[1]**2)**(0.5)
    dist.append((i[0],i[1],d,))
k = 2
dist.sort(key = lambda x:x[2])
points.clear()
for i in range(k):
    points.append([dist[i][0],dist[i][1]])    