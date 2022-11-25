#!/usr/bin/env python3
# coding: utf8

# Skyscraper height

from functools import reduce

def calculate_height_diffs(l) -> int:
    diffs = []
    for item, i in zip(l, range(0, len(l))):
        if i != 0:
            diffs.append(abs(item - l[i - 1]))

    return reduce(lambda x,y: x+y, diffs)

def main():
    calculate_height_diffs([int(x) for x in str(2**1024)])
    
    
if __name__ == "__main__":
    main()