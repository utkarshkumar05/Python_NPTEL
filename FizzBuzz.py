# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 19:41:48 2021

@author: utkarsh kumar
"""


for i in range(1,51):
    if(i%3==0):
        print(str(i)+" = Fizz")
    elif(i%5==0):
        print(str(i)+" = Buzz")
        if(i%3==0 and i%5==0):
            print(str(i)+" = FizzBuzz")
    else:
        print(str(i))