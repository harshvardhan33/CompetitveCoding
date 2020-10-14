# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 14:31:48 2020

@author: harshvardhan
"""
class Node:
    def __init__(self):
        self.alpha = [None for i in range(26)]
        self.end = False

class TrieNode:
    def __init__(self):
        self.root = Node()
        
    def insert(self,word):
        curr = self.root
        for i in word:
            curr_alpha = i
            idx = ord(curr_alpha)-ord("a")
            if curr.alpha[idx] is None:
                curr.alpha[idx] = Node()
            curr = curr.alpha[idx]
        curr.end = True
        
    def search(self,word):
        curr = self.root 
        for i in word:
            curr_alpha = i 
            idx = ord(curr_alpha)-ord("a")
            if curr.alpha[idx] is None:
                return False
            else:
                curr = curr.alpha[idx]
        if curr.end ==True:
            return True
        else:
            return False
    
    def startsWith(self,word):
        ans = True
        curr = self.root
        for i in word:
            curr_alpha = i 
            idx = ord(curr_alpha)-ord("a")
            if curr.alpha[idx] is not None:
                curr = curr.alpha[idx]
            else:
                ans = False
        
        return ans




obj = TrieNode()
obj.insert("harsh")
obj.insert("app")
print(obj.search("harsh"))
print(obj.search("ap"))
print(obj.startsWith("ap"))