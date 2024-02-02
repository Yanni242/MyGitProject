#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 11:19:51 2023

@author: sethblundell
"""


#########################
# Course: COMP 1113 FA02, 2023
# Lab 7
# Author <Seth Blundell>
# Student ID: <0303322b>
# Email Address: 0303322b@acadiau.ca
# Date: <2023-10-26 / 2023-10-26>
# I certify that this code is my own. I have not broken any rules concerning Academic Dishonesty.
#########################
import random
import operator

def SumFactors(x):
    sumOfFactor = 0
    for y in range(1, x + 1):
        if x % y == 0:
            sumOfFactor += y
    return sumOfFactor

def multiplyTwo(x):
    num = x
    num *= 2
    return num

def factorize(x):
    result = 1
    for i in range(2, x + 1):
        result *= i
    return result

def magic(x):
    # Dictionary mapping operations to their corresponding functions
    ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    
    # Select a random operation
    op = random.choice(list(ops.keys()))
    rand_num = random.randint(1, 20)
    result = ops[op](x, rand_num)
    return result


def quiz():
    print("A) factorial")
    print("B) number * 2")
    print("C) sum of the factors")
    print("D) just some magic")
    
    

numberInput = int(input("Input a number please: "))
numberNumber = (SumFactors(numberInput))
print(f"Your new number is: {numberNumber}")

while True:
    print("What do you think I did to your number?")
    quiz()
    finalAnswer = input("answer here (a, b, c, or d): ").lower()
    if finalAnswer != 'c':
        print("Try again")
    else:
        print("Correct!")
        break

