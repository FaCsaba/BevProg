#!/usr/bin/env python3
# coding: utf8

# Homework 2:
#   Math stuff yaaay!!
# In this excersize we have to find 3 formulas, and implement them in python

from functools import reduce
from math import sqrt
from typing import Dict, List, Tuple, AnyStr


def masodfoku(a, b, c) -> Tuple[float, float]: # Másodfokú egyenlet, doesn't handle edge cases!!
    return (-b+sqrt(b**2-4*a*c)/2*a), (-b-sqrt(b**2-4*a*c))/2*a

# Weighted average formula
# Input is a list of dictionary that has a weight and a value
def weightedaverage(to_be_averaged: List[Dict[AnyStr, int]]):
    weighted_value = 0
    for x in to_be_averaged:
        weighted_value += x["weight"]*x["value"]
    
    sum_of_weight = 0
    for x in to_be_averaged:
        sum_of_weight += x["weight"]

    return weighted_value / sum_of_weight

# Standard deviation calculation
# √(Sum(|x-averge(x)|^2)/n)
def standard_deviation(l: List[int]):
    average = sum(l) / len(l)
    s = 0.0
    for x in l:
        s += abs(x-average)**2
    return sqrt(s / len(l))

def main():
    print(masodfoku(2, 10, 3))
    print(weightedaverage([{"weight": 25, "value": 75}, {"weight": 30, "value": 60}]))
    print(standard_deviation([9, 2, 5, 4, 12, 7, 8, 11, 9, 3, 7, 4, 12, 5, 4, 10, 9, 6, 9, 4]))


if __name__ == "__main__":
    main()