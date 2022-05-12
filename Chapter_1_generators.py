# -*- coding: utf-8 -*-
"""
Created on Wed May 11 17:51:27 2022

@author: LENOVO
"""

def fibonacci():
    a=0
    b=1
    while True: # keep going...
        yield a # report value, a, during this pass
        future = a + b
        a=b # this will be next value reported
        b = future

if __name__ == "__main__":
    number_f = int(input("Enter the Fibonacci number position:\n"))
    init_fibonacci = fibonacci()
    for i in range(0,number_f+1):
        next(init_fibonacci)
        if i == number_f:
            print("Your Fibonacci number is:", next(init_fibonacci))