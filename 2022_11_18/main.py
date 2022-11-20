#!/usr/bin/env python3
# coding: utf8

# Main file

import modules

def main():
    modules.hello()
    modules.sayHiToUser(input("What is your name? "))

if __name__ == "__main__":
    main()