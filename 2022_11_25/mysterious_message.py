#!/usr/bin/env python3
# coding: utf8

# Mysterious Message

import os

ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()

def shift(t: str, n: int) -> str:
    if t in ABC:
        i = ABC.find(t)
        if i >= 127:
            raise ValueError("we only use the ascii table")

        return ABC[(i-n) % len(ABC)]
    else:
        i = abc.find(t)
        if i >= 127:
            raise ValueError("we only use the ascii table")

        return abc[(i-n) % len(abc)]

def main():
    with open(os.path.join(os.path.dirname(__file__), "message"), "r") as f:
        s = ord("K") - ord("M")
        shifted = "".join([shift(x, s) if x in ABC or x in abc else x for x in f.read()])
        print(shifted)

if __name__ == "__main__":
    main()