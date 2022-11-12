#!/usr/bin/env python3
# coding: utf8

# File reading

import json
import os

def main():
    
    if not os.getcwd().__contains__("2022_11_11"):
        print("you should be in the 2022_11_11 folder")
        exit(1)
    
    f = open("./something", 'r')
    content = f.readlines()
    print(content)
    f.close()
    
    f = open("./something", 'a')
    for i in range(0, 10):
        print(i, file=f)
    f.close()
    
    f = open("./something", 'w')
    print("Just a world", file=f)
    f.close()
    
    with open("./something") as f:
        something = f.read()
        print(something)

    

if __name__ == "__main__":
    main()