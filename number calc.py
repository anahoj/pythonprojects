#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 17:05:34 2025

@author: jac
"""
while True:
    number = input("phone number? ")
    if number == "done":
        break
    else:
        digits = [int(n) for n in number]
        n2s = digits.count(2)
        n4s = digits.count(4)
        n8s = digits.count(8)
        sums = sum(digits)

        while sums > 9:
            sums = sum([int(d) for d in str(sums)])

        print("sum: " + str(sums))
        print("2s: " + str(n2s))
        print("4s: " + str(n4s))
        print("8s: " + str(n8s))
        
        if n2s > 1:
            print("not the best number\n")
        elif n4s > 1:
            print("not the best number\n")
        elif n8s > 0:
            print("not the best number\n")
        elif sums == 8:
            print("not the best number\n")
        elif sums == 1:
            print("good number\n")
        else:
            print("okay number\n")

