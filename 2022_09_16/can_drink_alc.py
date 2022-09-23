#!/usr/bin/env python3
# coding: utf8

def main():
    age = int(input("What is your age: "))

    if age >= 21:
        print("You can! (even in America)")
    elif age >= 18:
        print("You can! (at least in Europe)")
    else:
        print("Nope. Sorry!")


if __name__ == "__main__":
    main()
