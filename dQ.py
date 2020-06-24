# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 21:38:53 2020

@author: harshvardhan
"""

from collections import deque as dQ

d = dQ()
d.append(1)
d.appendleft(2)
d.append(1)
d.appendleft(2)
d.popleft()
d.pop()
print(d)

# TO maintain a minmax queue we can use both the end 
# of the queue as min max ends 
# fix one end for each 
