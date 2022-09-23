#!/usr/bin/env python3
# coding: utf8
# \o/ loops!!

def main(): 
    # for .. in .. loop:
    for i in range(0, 9, 2):
        print("HI!!")
    
    # for in a range object does it n times
    for i in range(5):
        print(i)
        
    # for in a list object
    li = ["alma", "körte", "szilva", "szőlő"]
    for i in li:
        print(i)
    
    # while loop
    i = 0
    while i < 5:
        print(i)
        i += 1
    
    i = 1
    while i < 15:
        if (i % 2 == 0) and (i % 3 == 0):
            break
        print(i)
        i += 1

if __name__ == "__main__":
    main()