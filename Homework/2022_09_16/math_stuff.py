#!/usr/bin/env python3
# coding: utf8

# Homework 2:
#   Math stuff yaaay!!
# In this excersize we have to find 3 formulas, and implement them in python

from math import sqrt
from typing import Tuple


def masodfoku(a, b, c) -> Tuple[float, float]: # Másodfokú egyenlet, doesn't handle edge cases!!
    return (-b+sqrt(b**2-4*a*c)/2*a), (-b-sqrt(b**2-4*a*c))/2*a



def main():
    print(type(masodfoku(2, 10, 3)))


if __name__ == "__main__":
    main()
    input()