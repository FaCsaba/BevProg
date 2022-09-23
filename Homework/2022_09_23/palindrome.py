#!/usr/bin/env python3
# coding: utf8

# Homework: 3
# Palindromes
# Numbers which are the same forward as they are backwards
# Check wether a number is a palindrome or not

def is_palindrome(number: int) -> bool:
    a = str(number)
    b = "".join(list(reversed(a)))
    return a == b


def main():
    print(is_palindrome(1234321))  # Are palindromes
    print(is_palindrome(6996))
    print(is_palindrome(42024))
    print(is_palindrome(1))

    print(is_palindrome(12345))  # Are not palindromes
    print(is_palindrome(54321))
    print(is_palindrome(0x94234))
    print(is_palindrome(69420))


if __name__ == "__main__":
    main()
