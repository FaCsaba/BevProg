#!/usr/bin/env python3
# coding: utf8

# Anagram

from collections import Counter

def normalize(n: str):
    return "".join([x if x.isalnum() else "" for x in n.lower().strip()])

def is_anagram(a: str, b: str):
    a = Counter(a)
    b = Counter(b)
    print(a, b)
    return a == b
    

def main():
    print(normalize("Clint Eastwood"))
    print(is_anagram(normalize("Clint Eastwood"), normalize("Old west action")))
    pass

if __name__ == "__main__":
    main()