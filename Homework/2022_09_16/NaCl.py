#!/usr/bin/env python3
# coding: utf8

# Homework 3:
# We must ask the user for some amount of Na and some amount of Cl
# Based on those we must print out how many NaCl-s we could make
# if there are excessive amounts we must print that as well
# 2NaCl = 2Na + Cl2
from types import LambdaType
from typing import AnyStr


def handle_user_input(phrase: AnyStr, type: type, validation: LambdaType, validaiton_fail: AnyStr = None):
    while True:
        try:
            ret = type(input(phrase))
            if validation(ret):
                return ret
            elif not validaiton_fail == None:
                print(validaiton_fail)
        except ValueError:
            continue


def main():
    na = handle_user_input("How many Na-s do you have? ",
                           int, lambda x: x >= 0)
    cl2 = handle_user_input(
        "How many Cl\u2082-s do you have? ", int, lambda x: x >= 0)

    nacl = 0
    excess_na = 0
    excess_cl = 0

    if na == cl2*2:
        nacl = na
    if na > cl2*2:
        nacl = cl2*2
        excess_na = na - cl2*2
    if cl2*2 > na:
        nacl = na
        excess_cl = cl2*2 - na

    print("You can make {amount} NaCl, isn't that exciting".format(
        amount=nacl))
    if excess_na > 0:
        print("But you have excess of Na by {0}".format(excess_na))
    if excess_cl > 0:
        print("But you have excess of Cl by {0}".format(excess_cl))


if __name__ == "__main__":
    main()
