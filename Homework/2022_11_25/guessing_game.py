#!/usr/bin/env python3
# coding: utf8

# Guessing game

from random import randint

def main():
    num = randint(1, 100)
    guess = 0
    print("Guess a number between 1 and 100")
    while True:
        while True:
            try:
                guess = int(input("Give me a number: "))
                break
            except ValueError:
                continue
        if (guess < num):
            print("Your guess is less then the number")
        if (guess > num):
            print("Your guess is bigger then the number")
        if (guess == num):
            print("Congrats you got it")
            break
    

if __name__ == "__main__":
    main()