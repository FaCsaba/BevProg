#!/usr/bin/env python3
# coding: utf8

# Homework 4
def custom_bin(n: int) -> str:
    t = ""
    while True:
        t = f'{n % 2}{t}'
        n = n // 2
        if n == 0:
            break
    return f'0b{t}'


def main():
    assert (custom_bin(69) == bin(69))
    assert (custom_bin(100) == bin(100))
    assert (custom_bin(420) == bin(420))

    try:
        assert (custom_bin(9) == bin(69))
    except AssertionError:
        pass


if __name__ == "__main__":
    main()
