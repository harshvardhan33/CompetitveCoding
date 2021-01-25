# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 16:01:28 2020

@author: harshvardhan
"""
# Push O(n)
# Pop O(1)
from queue import Queue
class Stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
        self.curr_size = 0 
    
    def push(self,x):
        self.curr_size+=1
        if self.q1.empty():
            self.q1.put(x)
        else:
            while not self.q1.empty():
                temp = self.q1.get()
                self.q2.put(temp)
            
            self.q1.put(x)
            while not self.q2.empty():
                temp = self.q2.get()
                self.q1.put(temp)
            
    def pop(self):
        temp = self.q1.get()
        return temp
        self.curr_size-=1
        
        
    def top(self):
        if self.q1.empty():
            return -1
        return self.q1.queue[0]



q = Stack()
q.push(1)
q.push(2)
print(q.pop())
print(q.top())
print(q.pop())
        