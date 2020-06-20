# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 23:09:13 2020

@author: harshvardhan
"""

class Queue:
    def __init__(self,cap):
        self.size = cap
        self.q = []
        self.front = -1
        self.rear = -1
    
    def enq(self,val):
        if len(self.q)==self.size:
            print("oops no space")
        elif len(self.q)==0:
            self.front+=1
            self.rear+=1
            self.q.append(val)
            
        else:
            self.q.append(val)
            
            self.rear+=1
            
        
    def deq(self):
        if len(self.q)==0:
            print("Already empty Q")
        else:
            del self.q[self.front]
            self.rear-=1
            
    def getFront(self):
        if len(self.q)==0:
            print("Queue is empty")
            return -1
        return self.q[self.front]
        
    
    def getRear(self):
        if len(self.q)==0:
            print("Queue is empty")
            return -1
        return self.q[self.rear]
    
    
    def isFull():
        pass
    
    
    def isEmpty():
        pass
            
            
q = Queue(5)

q.enq(1)
q.enq(2)
q.enq(3) 
q.enq(4) 
q.enq(5)   
print(q.getFront())
print(q.getRear())
q.deq()
q.deq()
q.deq()
q.deq()
q.deq()
q.deq()
print(q.getFront())
print(q.getRear())
            