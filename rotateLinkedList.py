# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 15:14:16 2020

@author: harshvardhan
"""


# This code rotates the linked list by K places 



class Node:
    def __init__(self,val):
        self.next = None 
        self.val = val 



head = Node(1)
count = 2
temp = head 

while count<9:
    helper = Node(count)
    temp.next = helper 
    temp = helper 
    count+=1
    

k = 4
new_head = head 
prev = None
if k>0:
    while k:
        prev = new_head
        new_head = new_head.next
        k-=1
    prev.next =None
    
    last = new_head 
    while last.next is not None:
        last = last.next
    
    last.next = head

while new_head is not None:
    print(new_head.val)
    new_head = new_head.next
    