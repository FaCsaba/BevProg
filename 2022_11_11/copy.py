#!/usr/bin/env python3
# coding: utf8

import os

def main():

    if not os.getcwd().__contains__("2022_11_11"):
        print("you should be in the 2022_11_11 folder")
        exit(1)

    with open("something", 'r') as f, open("something2", 'w') as f2:
        f2.write(f.read())

if __name__ == "__main__":
    main()