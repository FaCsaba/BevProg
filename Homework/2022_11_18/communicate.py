#!/usr/bin/env python3
# coding: utf8

# Homework 9
# Using files to communicate between two programs

import os

def main():
    while True:
        try:
            inp = input("Send this to the other program: ")
            # os agnostic-ly getting to the file
            f = open(os.path.join(os.path.dirname(__file__), "communication"), "w+")
            print(inp, file=f)
            f.close()
        except:
            break

if __name__ == "__main__":
    main()