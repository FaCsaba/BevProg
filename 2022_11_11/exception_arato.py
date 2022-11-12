#!/usr/bin/env python3
# coding: utf8

# Homework 

def main():
    while True:
        try:
            n1 = float(input("1st num: "))
            n2 = float(input("2nd num: "))
            result = n1 / n2
            print("Result: {0:.2f}".format(result))
        except ValueError:
            print("That's not a number silly")
        except ZeroDivisionError:
            print("2nd number can not be zero, you can't divide by zero, smh🤦, but here's dividing with 1 for ya for free ;)")
            print("Result: {0:.2f}".format(n1))
        except KeyboardInterrupt:
            break



if __name__ == "__main__":
    main()