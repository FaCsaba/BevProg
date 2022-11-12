#!/usr/bin/env python3
# coding: utf8


def main():
    try:
        d1 = int(input("num1: "))
        d2 = int(input("num2: "))

        print(d1/d2)
    except ValueError:
        print("That is not a number!")
    except ZeroDivisionError:
        print("You cant divide with a zero")
    except KeyboardInterrupt:
        print("Bye bye")


    try:
        with open("__file__") as f:
            asdf = f.read()
            print(asdf)

    except FileNotFoundError:
        print("Oh oh")
    


if __name__ == "__main__":
    main()