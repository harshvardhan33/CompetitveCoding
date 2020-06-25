# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 22:36:53 2020

@author: harshvardhan
"""

  
# Euler totient Function 
def ETF(): 
  
    for i in range(1, n + 1): 
        phi[i] = i; 
  
    for i in range(2, n + 1): 
        if (phi[i] == i): 
            phi[i] = i - 1; 
            for j in range(2 * i, n + 1, i): 
                phi[j] = (phi[j] * (i - 1)) // i; 
  
# Function to return the required LCM sum 
def LcmSum(m): 
    ETF(); 
  
    for i in range(1, n + 1): 
  
        # Summation of d * ETF(d) where 
        # d belongs to set of divisors of n 
        for j in range(i, n + 1, i): 
            ans[j] += (i * phi[i]); 
  
    answer = ans[m]; 
    answer = (answer + 1) * m; 
    answer = answer // 2; 
    return answer; 
  
# Driver code 
n = 5
phi = [0] * (n + 2); 
ans = [0] * (n + 2);  
print(LcmSum(n)); 
  
# This code is contributed  
# by chandan_jnu 