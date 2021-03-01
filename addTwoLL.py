# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 11:46:24 2020

@author: harshvardhan
"""

# 3 6 5
# 2 4 8



class Node:
    def __init__(self,val):
        self.val = val 
        self.next = None 
        


first = Node(5)
first.next = Node(6)
first.next.next = Node(3)


second = Node(8)
second.next = Node(4)
second.next.next = Node(2)
second.next.next.next = Node(1)

carry = 0
res = []
while first is not None and second is not None:
    curr=0
    curr = first.val+second.val
    if carry>0:
        curr+=carry
    carry = curr//10
    res.append(curr%10)
    first = first.next
    second = second.next

while first:
    curr = 0 
    curr = first.val
    if carry>0:
        curr+=carry 
    carry = curr//10
    res.append(curr%10)
    first = first.next

while second:
    curr = 0 
    curr = second.val
    if carry>0:
        curr+=carry 
    carry = curr//10
    res.append(curr%10)
    second = second.next
    
    
print(res[::-1])

# Making a linked List of these nodes 

third = Node(res[0])
temp = third
for i in range(1,len(res)):
    temp.next = Node(res[i])
    temp = temp.next

while third is not None:
    print(third.val)
    third = third.next    