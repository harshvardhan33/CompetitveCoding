# -*- coding: utf-8 -*-
"""
Created on Wed May 12 12:56:19 2021

@author: harshvardhan
"""

import heapq as hq


# =============================================================================
# v,e = map(int,input().split())
# graph = {i:[] for i in range(v)}
# for i in range(e):
#     e1,e2,w = map(int,input().split())
#     graph[e1].append((e2,w))
#     graph[e2].append((e1,w))
# =============================================================================

graph = {0: [(1, 2), (3, 1)],
  1: [(0, 2), (4, 4), (2, 5)],
  2: [(1, 5), (4, 1)],
  3: [(0, 1), (4, 3)],
  4: [(1, 4), (3, 3), (2, 1)]}

v = 5
dist = [float("inf") for i in range(v)]
pq = []
hq.heapify(pq)

dist[0] = 0
pq = []
hq.heapify(pq)
# (Distance, Node) in PQ
hq.heappush(pq,(0,0))

while len(pq):
    u = hq.heappop(pq)
    # Graph has (Node,Distance)
    # Heap has (Distance,Node)
    for curr in graph[u[1]]:
        if dist[curr[0]]>u[0]+curr[1]:
            dist[curr[0]] = u[0]+curr[1]
            hq.heappush(pq,(dist[curr[0]],curr[0]))
            