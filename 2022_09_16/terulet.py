#!/usr/bin/env python3
# coding: utf8

# Todays class is about basic functions of the language. 
# Like getting input from the user and displaying it on the screen
# The input() method is used to get something from the user
# When we get this input we want to convert that to an integer
# If int fails with a ValueError we can catch it in a try catch block which in our case is actually a try expect block
# Because we expect it to fail with some kind of error 

# Constants are non existent in python. We declare them globally with uppercase like PI = 3

# If statements are pretty much the same as in every other language 

def main():
    is_num = False
    a = None
    b = None
    while not is_num:
        try:
            if not type(a) == int:
                a = int(input("Téglalap egyik oldala: "))
            if not type(b) == int:
                b = int(input("Téglalap másik oldala: "))
            is_num = True
        except ValueError:
            print("Not a number!")

    print("Terület: {t}".format(t = a*b))
    print("Kerület:", 2*(a+b))
    
    
if __name__ == "__main__":
    main()