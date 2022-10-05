#!/usr/bin/env python3
# coding: utf8

# Homework 3

def insert(text: str, insert_before: str, to_insert: str) -> str:
    l = list(text)
    if not insert_before in text:
        raise Exception(f"{insert_before} is not found in {text}")
    l.insert(text.find(insert_before), f"{to_insert} ")
    return "".join(l)


def main():
    print(insert("Az egy bögre", "bögre", "piros"))


if __name__ == "__main__":
    main()
