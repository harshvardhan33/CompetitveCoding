# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 15:20:35 2020

@author: harshvardhan
"""

"""
There are multiple methods to detect loop in a linked list 
1- store the address of nodes in a hash table if address comes up again, loop exist 
2- change the structure of the node in linked list 
    make a boolean variable inside the structure as visited 
    when ever you visit a node that has visited set as true you print yes there is a loop   
3- we can use the approach of the fast and slow pointer to do this 
"""



class Node:
    def __init__(self,val):
        self.val = val
        self.next = None


head = Node(1)
n = 2
helper = head
while(n<10):
    temp = Node(n)
    helper.next = temp
    helper = helper.next
    n+=1


# Uncomment this to check for a loop example 
#helper.next = head.next.next.next.next


# Method 1
ptr = head
dc = {}
while ptr is not None:
    if id(ptr) not in dc:
        dc[id(ptr)] = True
    else:
        print("There is a LOOP")
        break
    ptr = ptr.next
    
# Method 2  // fast and slow pointer
    
slow = head
fast = head

while fast is not None and fast.next is not None:
    slow = slow.next
    fast = fast.next.next
    if slow==fast:
        print("Yes loop")
        break
    