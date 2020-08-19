# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 16:01:28 2020

@author: harshvardhan
"""


from queue import Queue
class Stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
        self.curr_size = 0 
    
    def push(self,x):
        self.q1.put(x)
    
    def pop(self):
        while self.q1.qsize()!=1:
            temp = self.q1.get()
            self.q2.put(temp)
        
        ans = self.q1.get()
        while not self.q2.empty():
            temp = self.q2.get()
            self.q1.put(temp)
            
        return ans
        
    def top(self):
        pass


q = Stack()
q.push(1)
q.push(2)
print(q.pop())
#print(q.top())
print(q.pop())
        