# -*- coding: utf-8 -*-
"""
Created on Tue May 25 09:20:14 2021

@author: harshvardhan
"""


"""

n = 3
3! = 6 permutations 

123,132,213,231,312,321

Brute Force : Generate all permutation , sort them ,
return kth-1 index
Time Complexity : 
    n! : generation
    n : each recursionf or deep copy 
    n!logn! : sort 

Optimal Solution :
    Recursion
"""


def fact_calculate(num):
    if num==1:
        return 1 
    return num*fact_calculate(num-1)
    

n = 3
k = 3
nums = [i for i in range(1,n+1)]
fact = fact_calculate(n-1)
k = k-1 
res = ""

while True:
    # Select the num to begin
    res = res + str(nums[k//fact])
    # Remove the selected num
    nums.pop(k//fact)
    # If no numbers are left 
    if len(nums)==0:
        break
    # Process for remaining ones 
    k = k%fact
    fact = fact//len(nums)
    
    

