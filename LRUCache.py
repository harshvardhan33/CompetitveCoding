# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 19:28:54 2020

@author: harshvardhan
"""

class DLL:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None 
        
    


class LRU:
    def __init__(self,capacity):
        self.head = DLL(-1,-1)
        self.tail = self.head
        self.hash = {}
        self.capacity = capacity
        self.length = 0
        
    def get(self,key):
        if key not in self.hash:
            return -1
        node = self.hash[key]
        val = node.val
        while node.next:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.tail.next = node
            node.prev = self.tail
            node.next = None
            self.tail
        return val
    
    def put(self,key,value):
        if key in self.hash:
            node = self.hash[key]
            node.val = value
            while node.next:
                node.prev.next = node.next
                node.next.prev = node.prev
                self.tail.next = node
                node.prev = self.tail
                node.next = None
                self.tail = node
        else:
            node=DLL(key,value)
            self.hash[hash]=node
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.length+=1
            if self.length > self.capacity:
                remove = self.head.next
                self.head.next.prev = self.head
                del self.hash[remove.key]
                self.length-=1
        
    
