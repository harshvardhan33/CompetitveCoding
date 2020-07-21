# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 14:02:55 2020

@author: harshvardhan
"""



def method1(head,n):
    count = 0 
    temp = head
    while temp is not None :
        temp = temp.next
        count+=1
    
    temp  = head
    target = (count-n)
    while target:
        target-=1
        temp=temp.next
    print(temp.val)
    return 

def method2(head,n):
    first = second = head 
    while n:
        n-=1
        first = first.next
    
    while first is not None:
        first = first.next
        second = second.next 
    
    
    print(second.val)
    return 




class Node:
    def __init__(self,val):
        self.val= val 
        self.next = None 
        



head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next= Node(4)
head.next.next.next.next= Node(5)
head.next.next.next.next.next= Node(6)
head.next.next.next.next.next.next= Node(7)


method1(head,3)
method2(head,3)


