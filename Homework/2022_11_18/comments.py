#!/usr/bin/env python3
# coding: utf8

# Homework Removing comments

import os

def main():
    with open(os.path.join(os.path.dirname(__file__), "example.py"), "r") as f:
        lines = f.readlines()

        nw = "".join(filter(lambda x: x.strip() == "" or not x.strip()[0] == "#", lines))
        print(nw)

if __name__ == "__main__":
    main()