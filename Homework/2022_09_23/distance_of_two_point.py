#!/usr/bin/env python3
# coding: utf8

# Homework: 4
# Give the distance of two points based on their coordinates

import math

# formula for distance of two points 
# √((p1.x - p2.x)² + (p1.y - p2.y)²)
def distance(p1, p2):
    a = p2[0] - p1[0]
    b = p2[1] - p1[1]
    
    return math.sqrt(a*a + b*b)

def main():
    p1 = (1, 2)
    p2 = (6, 5)
    print('Distance of two points:', distance(p1, p2))

if __name__ == "__main__":
    main()