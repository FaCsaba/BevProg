#!/usr/bin/env python3
# coding: utf8

# Homework: 2
# get the nth number of a fibonacci sequence

# Approaches to the problem:
# using a for loop
# downloading a library :)  (as a javascript developer this is always the solution)
# using a recursive algorithm
# using a recursive algorithm with memoization
# Making a class and overloading the iterator
#   so we could do something like "for i in fib_object(5):"
#   which would always give us the next iteration of the fib sequence

# this could be done in a number of ways and I chose to showcase only a few

from typing import List

# using recursion!!
# recursion means a function definition contains a call to itself


def fib(i: int) -> int:
    if i in [0, 1]:  # We set up a base case so we don't loop forever
        return i    # (Well not forever but until we run out of stack frames)

    return fib(i-1) + fib(i-2)


# using a simple for loop


def fib_with_for(i: int) -> int:
    a = 0
    b = 1
    c = 0
    for _ in range(i):
        c = a + b
        b = a
        a = c

    return a

# using memoization
# Memoization means we pass a memorized value to the next recursion
# thus skipping a lot of unnecessary computation


def memoized_fib(i: int, memo: List[int]) -> int:

    if len(memo) > i:
        return memo[i]

    memo.append(memoized_fib(i-2, memo) + memoized_fib(i-1, memo))
    return memo[i]


def main():
    print(fib_with_for(20))
    print(fib(20))

    # we need a base case for our recursion
    # we could use a dictionary but this list could get fairly large
    # and the data structure for our recursion is not very complex
    memo = [0, 1]
    # Try upping this number! Check what your machine can handle ;)
    print(memoized_fib(69, memo))


if __name__ == "__main__":
    main()
