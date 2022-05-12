# -*- coding: utf-8 -*-
"""
Created on Wed May 11 17:03:56 2022

@author: Francis GVM
"""

def factors(n):
    for i in range(1,n+1):
        if n%i == 0: 
            yield i

try:
    for factor in factors(10**7):  # An instance of this generator is created 
        print(factor)
    
    for i in range(1,10**7+1):
        if 10**7%i == 0: 
            print(i)
except: 
    raise

finally:
    print("\nEnd")