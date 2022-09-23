#!/usr/bin/env python3
# coding: utf8
# Just a simple filtering function

def main():
    l1 = [1, 2, 3, 4, 5]
    l2 = [2, 69, 420, 3]

    print(list(filter(lambda x: x in l2, l1)))


if __name__ == "__main__":
    main()
