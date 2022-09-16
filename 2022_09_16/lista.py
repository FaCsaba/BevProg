#!/usr/bin/env python3
# coding: utf8

# Declaring Lists are done with brackets: [ ]
# Separating Lists by commas: ,

def main():
    li = ["alma", "barack", "banán"]
    li2 = list(("alma", "barack", "banán"))
    assert li == li2
    li.pop()
    li.append("mango")
    a = li.copy()
    li.sort()
    print(li)
    print(li.index("barack"))
    
    

if __name__ == "__main__":
    main()