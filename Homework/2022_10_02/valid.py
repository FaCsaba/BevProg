#!/usr/bin/env python3
# coding: utf8

# Homework 2
# We have a text and we want to get all the valid characters out of this text

def valid(text: str, chars: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") -> str:
    return "".join(map(lambda t: t if t in chars else "", text))


def main():
    print(valid("asdf", "a1f23s"))
    print(valid("Barking!"))
    print(valid("KL754", "0123456789"))
    print(valid("BEAN", "abcdefghijklmnopqrstuvwxyz"))


if __name__ == "__main__":
    main()
