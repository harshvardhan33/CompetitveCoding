# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 15:49:40 2020

@author: harshvardhan
"""

class Node:
    def __init__(self,val):
        self.next = None 
        self.random = None 
        self.val = val
        
        


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

head.random = head.next.next
head.next.random=head
head.next.next.random = head.next.next.next.next
head.next.next.next.random = head.next.next
head.next.next.next.next.random = head.next.next.next.next




clone_head = None
temp = head
set_head =None

while temp is not None:
    if clone_head is None:
        clone_head = Node(temp.val)
        helper = clone_head
        temp = temp.next
        set_head = 
        
    helper.next = Node(temp.val)
    helper = helper.next
    temp = temp.next
    
while clone_head is not None:
    print(clone_head.val)
    clone_head = clone_head.next
