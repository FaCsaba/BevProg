#!/usr/bin/env python3
# coding: utf8

def main():
    a: String = 'Text'
    a = 1
    print(type(a) == int)

    a = 'Hello'
    b = 'World'
    print(a + " " + b)
    
    a = 2   # 
    a += 3
    a *= 9
    a = a//7
    a = a**2
    a = a % 8
    a -= 1
    print(chr(a))
    
    print(ord("@"))

if __name__ == "__main__":
    main()